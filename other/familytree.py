import os

def draw ():
    for root, dirs, files in os.walk ('.'):
        for d in dirs:
            print ('\t'*root.count('\\'), '--',d)
        for f in files:
            print ('\t'*root.count('\\'), f)

def main ():
    draw()

main ()
