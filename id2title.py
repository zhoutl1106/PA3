import re

f = open('title2id.txt','r')
line = ""

all_title_dic = {}

for line in f:
    splits = line.split()
    all_title_dic[splits[1]] = splits[0]

f = open('rank_result.txt','r')

for line in f:
    splits = line.split(' ',1)
    print(all_title_dic[splits[0]] + " " + splits[1][0:-2])
