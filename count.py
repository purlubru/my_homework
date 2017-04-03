def pointsaway (file):
    file = file.split()
    for i, word in enumerate (file):
        file[i] = file[i].strip('.,?!()*&^%$#@-_+=«»:;')
        file[i] = file[i].lower()
    return file

def words (file):
    slova = {}
    for word in file:
        if word in slova:
            slova[word] += 1
        else:
            slova[word] = 1
    return slova

def creation (dic):
    f = open ('file.tsv', 'w', encoding = 'utf8')
    arr = []
    for k in dic:
        arr.append(k)
    arr.sort()
    for i in arr:
        f.write(i + '\t' + str(dic[i]) + '\n')
    f.close()

def main ():
    f = open ('file.txt', 'r', encoding = 'utf8')
    file = f.read()
    f.close()
    text = pointsaway (file)
    semua = words (text)
    creation (semua)
    
main ()
