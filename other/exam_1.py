import re

#def pointsaway (file):
    

def find_w (file):
    words = re.findall('<w>', file)
    n = len(words)
    return n

def find_ana (file):
    anas = re.findall('<ana', file)
    n = len(anas)
    return n

def main ():
    f = open ('/home/woods/Загрузки/text.xml', 'r', encoding = 'utf8')
    file = f.read()
    f.close()
    words = find_w(file)
    anas = find_ana(file)
    result = anas/words
    print ('среднее количество разборов на слово', result)

main ()
