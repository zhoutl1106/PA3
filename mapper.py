#!/usr/bin/env python

import sys
import os
import re
from HTMLParser import HTMLParser

reload(sys)
sys.setdefaultencoding('utf8')

f = open('title2id.txt','r')

all_titles = []

for line in f:
    splits = line.split()
    all_titles.append(splits[0])

f = open('data/simplewiki-20170401-pages-meta-current.xml','r')
allPages = re.findall("<page.*?\</page>", f.read(),re.S)
h = HTMLParser()

for page in allPages:
    title = re.findall("<title>.*?\</title>",page,re.S)
    title = title[0][7:-8]
    if title in all_titles:
        body = re.findall("<text.*?\</text>",page,re.S)
        if len(body) > 0:
            body = body[0]
            body = body[body.find(">")+1:-7]
            body = h.unescape(body)
            # split the line into words
            words = body.split()
            processedWords = []

            for word in words:
                string = re.sub(r"[\W_\d]", "",word)
                # string = word
                if string not in processedWords and string != "":
                    processedWords.append(string)
                    pattern = re.compile(re.escape(string))
                    cnt = len(pattern.findall(body))
                    # write the results to STDOUT (standard output);
                    # what we output here will be the input for the
                    print '%s\t%s\t%s' % (string, title, cnt)
