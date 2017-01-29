import re

def pointsaway (file):
    file = file.split()
    for i, word in enumerate (file):
        file[i] = file[i].strip('.,?!()*&^%$#@-_+=«»:;')
        file[i] = file[i].lower()
    return file

def findverbs (file):
    verbs = []
    for word in file:
        if re.search ('загру(з(и.*|ят.*)|ж(у.*|ен.*))', word) != None:
            if word not in verbs:
                verbs.append(word)
    return verbs

f = open ('file_9.6.txt', 'r', encoding = 'utf8')
file = f.read()
file = pointsaway(file)
verbs = findverbs(file)
print (verbs)
