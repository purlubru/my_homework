import random

def intothedic (file):
    dic={}
    for line in file:
        line = line.split(';')
        for j, word in enumerate(line):
            line[j] = word.strip('\n')
        dic[line[0]] = line[1]
    return dic

def youchoose (dic):
    keys = []
    for key in dic:
        keys.append(key)
    return random.choice(keys)

def thegameison (noun, dic):
    for key in dic:
        if key == noun:
            hint = dic[key]
            n=key
            break
    print (hint, '...')
    for i in range (3):
        if input() == n:
            print ('Победа!')
            break
        else:
            if i == 0:
                print ('Ещё 2 попытки')
                continue
            elif i == 1:
                print ('Ещё 1 попытка')
                continue
            else:
                print ('GAME OVER')

f = open('file_8.6.csv', 'r', encoding = 'utf8')
file = f.readlines()
f.close()
words = intothedic(file)
word = youchoose(words)
thegameison(word, words)
