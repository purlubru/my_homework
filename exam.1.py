import os
import re

def files():
    ff = {}
    folder = 'news'
    for file in os.listdir(folder):
     with open(os.path.join(folder, file)) as text:
         words = re.findall('<w>', text.read())
         ff[file] = len(words)
    return ff

def newfile(dic):
    f = open('words_in_files.txt', 'w', encoding = 'utf8')
    s = ''
    for k in dic:
        s = k + '\t' + str(dic[k]) + '\n'
        f.write(s)
        s = ''
    f.close

def main ():
    ff = files()
    newfile(ff)

main()
