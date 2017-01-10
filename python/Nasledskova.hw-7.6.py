def pointsaway (file):
    file = file.split()
    for i, word in enumerate (file):
        file[i] = file[i].strip('.,?!()*&^%$#@-_+=«»:;')
        file[i] = file[i].lower()
    return file

def findomni (file):
    omni = []
    for word in file:
        if word.startswith('omni'):
            w = word.replace('omni', '')
            omni.append([word, w])
    return omni

def findwords (array, file):
    n = 0
    m = 0
    for i, k in enumerate (array):
        for word in file:
            if word == array[i][0]:
                n += 1
            if word == array[i][1]:
                m += 1
        print (array[i][0], n, '-', array[i][1], m)
        n = 0
        m = 0

def main ():
    name = input('Введите имя файла ')
    f = open (name, "r")
    file = f.read()
    f.close()
    file = pointsaway (file)
    findwords(findomni(file), file)

main()
    
