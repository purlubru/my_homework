import os
import re

def get_author (text):
    for word in text:
        if 'name="author"' in word:
            result = re.search('content="(.+?)"', word)
            return result.group(1)

def get_day (text):
    for word in text:
        if 'name="created"' in word:
            result = re.search('content="(.+?)"', word)
            return result.group(1)

def file_inf():
    ff = []
    folder = 'news'
    for file in os.listdir(folder):
        with open(os.path.join(folder, file)) as text:
            text = text.read().split('<')
            ff.append([file, get_author(text), get_day(text)])
    return ff

def newfile(arr):
    f = open('files_info.csv', 'w', encoding = 'utf8')
    f.write('Название файла;Автор;Дата создания текста\n')
    s = ''
    for i in arr:
        s = i[0] + ';' + i[1] + ';' + i[2] + '\n'
        f.write(s)
        s = ''
    f.close

def main ():
    ff = file_inf()
    newfile(ff)

main()
