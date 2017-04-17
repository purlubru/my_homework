import os

def findanddel (folder):
    for root, dirs, files in os.walk(folder, topdown = False):
        for f in files:
            os.remove(os.path.join(root, f))
        for d in dirs:
            os.remove(os.path.join(root, d))

def main ():
    folder = input()
    findanddel (folder)

main ()
