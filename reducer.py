#!/usr/bin/env python

from operator import itemgetter
import sys
reload(sys)
sys.setdefaultencoding('utf8')
current_word = None
current_lineNum = []
word = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    # if " " in line:
    try:
        word, title, cnt = line.split('\t', 3)
    except:
        print("Error line : ", line)
    cnt = int(cnt)

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    record = title+"_"+str(cnt)

    if current_word == word:
        current_lineNum.append(record)
    else:
        if current_word:
            # write result to STDOUT
            print(current_word, current_lineNum)
        current_lineNum = [record]
        current_word = word

# do not forget to output the last word if needed!
if current_word == word:
    print(current_word, current_lineNum)
