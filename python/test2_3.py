import re

def filework():
    f = open('corpus.txt', 'r', encoding = 'utf8')
    file = f.readlines()
    f.close()
    return file

def findthem (file):
    types = {}
    for line in file:
        a = re.search('<w lemma="(.+?)" type="(l.f.+?)">(.+?)</w>', line)
        if a:
            if a.group(2) not in types:
                types[a.group(2)] = 0
    return types

def countthem (file, types):
    words = []
    sum = 0
    for key in types:
        words.append(key)
    for el in words:
        for line in file:
            if '"'+el+'"' in line:
                sum += 1
        types[el] = sum
        sum = 0
    return types

def newfile (types):
    s = ''
    f = open('adj.txt', 'w', encoding = 'utf8')
    for key in types:
        s = s + key + '-' + str(types[key]) + '\n'
    f.write(s)
    f.close()
            
def main():
    text = filework()
    dic = findthem(text)
    dic = countthem (text, dic)
    newfile(dic)

main()
