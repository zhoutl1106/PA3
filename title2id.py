import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

f = open('data/simplewiki-20170401-all-titles','r')
fo1 = open('title2id.txt','w')
line = ""

id = 0
all_title_dic = {}
all_id_dic = {}

f.readline()
for line in f:
    splits = line.split()
    if len(splits) > 1:
        all_title_dic[splits[1]] = id
        all_id_dic[id] = splits[1]
        # print(splits[0],splits[1],id)
        fo1.write(splits[1] + " " + str(id) + "\n")
        id = id + 1

f = open('data/simplewiki-20170401-pages-meta-current.xml','r')
# f = open('data/short.xml','r')
fo = open('table.txt','w')
# fh_str = f.read()
allPages = re.findall("<page.*?\</page>", f.read(),re.S)
# print(len(allPages))
# idx = 0
for page in allPages:
    title = re.findall("<title>.*?\</title>",page,re.S)
    title = title[0][7:-8]
    if title in all_title_dic:
        links = re.findall("\[\[.*?\]\]",page,re.S)
        cnt = len(links)
        for link in links:
            link = link[2:-2]
            if link in all_title_dic:
                fo.write(str(all_title_dic[title]) + " " + str(all_title_dic[link]) + "\n")
                # fo.write(title + " " + link + "\n")
