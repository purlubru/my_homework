import os

def search ():
    exroot = '.'
    sum = 0
    types = []
    for root, dirs, files in os.walk('.'):
        if (exroot != root) or (root == '.'):
            for file in files:
              n = file.rfind('.')
              if file[(n+1):] not in types:
                  types.append(file[(n+1):])
            if len(types)<len(files):
                sum += 1
        exroot = root
        types = []
    print (sum)

def main ():
    search()

main ()
