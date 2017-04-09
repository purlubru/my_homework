def pointsaway (file):
    file = file.replace('?!', '.')
    file = file.split('.')
    for i, word in enumerate (file):
        file[i] = file[i].replace('.,?!()*&^%$#@-_"+=«»:;\n', '')
        file[i] = file[i].replace('-- ', ' ') 
        file[i] = file[i].lower()
    return file

def tenplus (text):
    for sentence in text:
        sentence = sentence.split()
        n=0
        s=0
        for word in sentence:
            word = word.strip('.,?!()*&^%$#@-_"+=«»:;\n')
            s+=len(word)
            n+=1
        if n>10:
            print ("Это предложение со словами длины %s"%(str(round(s/n, 1))))    

def main ():
    f = open ("file_12.6.txt", "r", encoding = "utf8")
    file = f.read()
    f.close()
    text = pointsaway (file)
    tenplus (text)

main ()
