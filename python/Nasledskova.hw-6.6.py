import random
file=open ('file_6.6.txt', 'r')

def noun():
    nouns=[]
    for line in file:
        if ' n ' in line:
            line=line.split(' ')
            nouns.append(line[0])
    file.seek(0, 0)
    return random.choice(nouns)

def pronoun():
    pronouns=[]
    for line in file:
        if ' pn ' in line:
            line=line.split(' ')
            pronouns.append(line[0])
    file.seek(0, 0)
    return random.choice(pronouns)

def verb():
    verbs=[]
    for line in file:
        if ' v ' in line:
            line=line.split(' ')
            verbs.append(line[0])
    file.seek(0, 0)
    return random.choice(verbs)

def adjective ():
    adjectives=[]
    for line in file:
        if ' adj ' in line:
            line=line.split(' ')
            adjectives.append(line[0])
    file.seek(0, 0)
    return random.choice(adjectives)

def suborob (n, adj, pn):
    x=random.randint(0,1)
    if x==0:
        return pn
    else:
        y=random.randint(0,1)
        if y==0:
            return n+' '+adj
        else:
            return n+' '+pn

def declarative (subj, v, obj):
    return subj.capitalize()+' '+v+' '+obj+'.'

def question (subj, v):
    x=random.randint (0, 1)
    if x==0:
        return 'Apa'+' '+subj+' '+v+'?'
    else:
        return 'Siapa'+' '+v+'?'

def negative (subj, v, obj):
    x=random.randint(0, 1)
    if x==0:
        return subj.capitalize()+' tidak '+v+' '+obj+'.'
    else:
        return subj.capitalize()+' bukan '+obj+'.'

def imperative (v, obj):
    x=random.randint(0,1)
    if x==0:
        return v.capitalize()+' '+obj+'!'
    else:
        return 'Jangan '+v+' '+obj+'!'

def conditional (subj1, v1, obj1, subj2, v2, obj2):
    return 'Kalau '+subj1+' '+v1+' '+obj1+', '+subj2+' '+v2+' '+obj2+'.'

def sequence ():
    a=[1, 2, 3, 4, 5]
    b=[]
    for i in range (5):
        x=random.choice(a)
        while x in b:
            x=random.choice(a)
        b.append(x)
    return b

def text():
    seq=sequence()
    for i in range (5):
        if seq[i]==1:
            print(declarative(suborob(noun(), adjective(), pronoun()), verb(), suborob(noun(), adjective(), pronoun())))
        elif seq[i]==2:
            print (question(suborob(noun(), adjective(), pronoun()), verb()))
        elif seq[i]==3:
            print (negative(suborob(noun(), adjective(), pronoun()), verb(), suborob(noun(), adjective(), pronoun())))
        elif seq[i]==4:
            print (imperative(verb(), suborob(noun(), adjective(), pronoun())))
        else:
            print (conditional(suborob(noun(), adjective(), pronoun()), verb(), suborob(noun(), adjective(), pronoun()), suborob(noun(), adjective(), pronoun()), verb(), suborob(noun(), adjective(), pronoun())))
            
text()
file.close
