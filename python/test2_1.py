def filework ():
    f = open('corpus.txt', 'r', encoding = 'utf8')
    file = f.readlines()
    f.close()
    return file

def newfile (text):
    f = open('lines.txt', 'w', encoding = 'utf8')
    f.write(str(len(text)))
    f.close

def main():
    text = filework()
    newfile(text)

main()
