import os

def names(array):
    names = []
    for name in array:
        if not os.path.isdir(name):
            names.append(name)
    return names

def haspoints(array):
    points = '.,!_-'
    s = 0
    su = 0
    for name in array:
        for c in name:
            if c in points:
                s += 1
        if s > 0:
            su += 1
        s = 0

    print ("Знаки препинания есть в названии такого количества файлов: ", su)

def main():
    files = names (os.listdir('.'))
    print (files)
    haspoints (files)

main()