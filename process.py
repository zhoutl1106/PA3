import ast
from operator import itemgetter
aggregateDic = {}
file = open('./reduce_result.txt','rt')
fpage = open('./sorted_rank_w_title.txt','rt')
fword = open('./total_words.txt','rt')

def grabAWord(word):
    file.seek(0)
    # read in each line to find querying word
    while True:
        line = file.readline().strip();
        if line == "":
            return []
        tempList = ast.literal_eval(line)
        if word == tempList[0]:
            return tempList[1]

def grabAPage(page):
    fpage.seek(0)
    # read in each line to find querying word
    while True:
        line = fpage.readline().strip();
        if line == "":
            return -1.0
        lines = line.split();
        if page == lines[0]:
            return float(lines[1][0:-1])

def grabTotalWord(title):
    fword.seek(0)
    # read in each line to find querying word
    while True:
        line = fword.readline().strip();
        if line == "":
            return 0
        lines = line.split();
        if title == lines[0]:
            return int(lines[1])

def process(word):

    f = open('title2id.txt','r')
    line = ""
    ret = ""

    all_title_dic = {}

    for line in f:
        splits = line.split()
        all_title_dic[splits[0]] = splits[1]

    if word in all_title_dic:
        ret = ret + "<h1>There is a page titled with " + word + "</h1>"

    # query each word
    queryResult = grabAWord(word)

    ret = ret + "<h1> Query Result : " + word + "</h1>"
    if len(queryResult) == 0:
        ret = ret + "not exist"
    else:
        tempResult = []
        for pos in queryResult:
            title, cnt = pos.split('_')
            total = grabTotalWord(title)
            pagerank = grabAPage(title)
            # if pagerank > 0:
            score = int(cnt) / total * 0.5 + pagerank / 104.59059628 * 0.5
            tempResult.append([title, cnt, total, pagerank, score])

        tempResult.sort(key=lambda x: x[4])
        tempResult.reverse()
        ret = ret + '<table style="width:100%"<tr><th>title</th><th>cnt in page</th><th>Total words in page</th><th>Page Rank</th><th>Score</th></tr>'
        for pos in tempResult:
                ret = ret + '<tr><th>' + pos[0] + "</th><th>" +pos[1] + "</th><th>" + str(pos[2])+ "</th><th>" + str(pos[3]) + "</th><th>"+str(pos[4])+"</th></tr>"
        ret = ret + '</table>'

    return ret
