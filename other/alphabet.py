def pointsaway (file):
    file = file.split()
    for i, word in enumerate (file):
        file[i] = file[i].strip('.,?!()*&^%$#@-_+=«»:;')
        file[i] = file[i].lower()
    return file

def creation (text):
    f = open ('new.txt', 'w', encoding = 'utf8')
    dic = {text[x]: x for x in range(0, len(text))}
    arr = [k for k in dic]
    arr.sort()
    for i in arr:
        f.write('{}\t{}\n'.format(i, str(dic[i])))
    f.close()

def main ():
    f = open ('file.txt', 'r', encoding = 'utf8')
    file = f.read()
    f.close()
    text = pointsaway (file)
    creation (text)
    
main ()
