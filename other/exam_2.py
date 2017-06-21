import re
    
def find_and_count (file):
    pos = {}
    for word in file:
        result = re.search('.*?gr="(\w+)', word) #программа смотрит только первый разбор, а надо смотреть все
        if result:
            if result.group(1) not in pos:
                pos[result.group(1)] = 1
            else:
                pos[result.group(1)] += 1
    return pos

def newfile (dic):
    f = open('pos.txt', 'w', encoding = 'utf8')
    s = ''
    for k in dic:
        s = s + k + '\t' + str(dic[k]) + '\n'
    f.write(s)
    f.close

def main ():
    f = open ('/home/woods/Загрузки/text.xml', 'r', encoding = 'utf8')
    file = f.read()
    text = file.split('\n')
    f.close()
    pos = find_and_count(text)
    newfile (pos)

main ()
