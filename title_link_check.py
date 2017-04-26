import re
import sys
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf8')

f = open('title2id.txt','r')
line = ""

all_title_dic = {}

for line in f:
    splits = line.split()
    all_title_dic[splits[0]] = 0



f = open('data/simplewiki-20170401-pages-meta-current.xml','r')
f1 = open('incoming_links_cnt.txt','wt')
f2 = open('total_words.txt','wt')

allPages = re.findall("<page.*?\</page>", f.read(),re.S)
h = HTMLParser()

for page in allPages:
    title = re.findall("<title>.*?\</title>",page,re.S)
    title = title[0][7:-8]
    if title in all_title_dic:
        body = re.findall("<text.*?\</text>",page,re.S)
        if len(body) > 0:
            body = body[0]
            body = body[body.find(">")+1:-7]
            body = h.unescape(body)
            # split the line into words
            words = body.split()
            f2.write(title + "\t" + str(len(words))+ "\n")

        links = re.findall("\[\[.*?\]\]",page,re.S)
        for link in links:
            link = link[2:-2]
            if link in all_title_dic:
                all_title_dic[link] = all_title_dic[link] + 1

print("***\n")

for k in all_title_dic:
    if all_title_dic[k] > 1:
       f1.write(k + " " + str(all_title_dic[k]) + "\n")
