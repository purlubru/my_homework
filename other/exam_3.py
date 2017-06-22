import re

def get_word (word):
    result = re.search('.*?<w>(\w+)', word)
    if result:
        return result.group(1)
    else:
        return None
    
def find_ins (text):
    inst = {}
    for i, word in enumerate(text):
        if 'gr="S' in word:
            if 'ins' in word:
                inst[i]=word
    return inst

def newfile (words, text):
    f = open ('ins.txt', 'w', encoding = 'utf8')
    s = ''
    for k in words:
        i = 0
        j = 1
        while i<3:
            if get_word(text[k-j]) != None:
                s = get_word(text[k-j])+ ' ' + s
                i += 1
                j += 1
            else:
                j += 1
        s = s + '\t' + get_word(words[k]) + '\t'
        i = 0
        j = 1
        while i<3:
            if get_word(text[k+j]) != None:
                s = s + ' ' + get_word(text[k+j])
                i += 1
                j += 1
            else:
                j +=1
        f.write(s)
    f.close

def main ():
    f = open ('/home/woods/Загрузки/text.xml', 'r', encoding = 'utf8')
    file = f.read()
    text = file.split('\n')
    f.close()
    ss = find_ins(text)
    newfile (ss, text)

main ()
