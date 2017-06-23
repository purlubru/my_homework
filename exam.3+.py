import os
import re

def tagsaway(sentence):
    s = ''
    for word in sentence:
        word = re.sub(u'<.+?>', u'', word)
        s = s + word + ' '
    return s #вот здесь я хочу выттащить всё предложение, в котором есть биграмма

def get_bigramms(text):
    bi = []
    text = text.split('<w>')
    for i, word in enumerate(text):
        if 'gr="A=' and 'gen' in word:
            if i+1 < len(text):
                w = text[i+1]
                if 'gr="S,' and 'gen' in w:
                    result1 = re.search('</ana>(.+?)</w>', word) #тут он должен находить биграммы
                    result2 = re.search('</ana>(.+?)</w>', w)
                    bi.append([result1.group(1), result2.group(1), tagsaway(text)])
    return bi

def newfile(arr):
    f = open('bigramms.txt', 'w', encoding = 'utf8')
    s = ''
    for i in arr:
        s = i[0] + '\t' + i[1] + '\t' + i[2] + '\n'
        f.write(s) #тут я записываю информацию в файл, но получается плохо, там везде \n, которые мне не нужны
        s = ''
    f.close

def filework():
    folder = 'news'
    for file in os.listdir(folder):
        with open(os.path.join(folder, file)) as text:
            text = text.read().split('<se>') #отправляю текст на поиск биграмм по предложению
            for se in text:
                newfile(get_bigramms(se))

def main ():
    filework()

main()

#Я не успела доделать
#Моя программа даже находит что-то, но не то, понять, где проблема, у меня уже нет времени, простите(
