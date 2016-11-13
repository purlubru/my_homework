xs=[]
for i in range (7):
    xs.append(int(input()))
for i in range (7):
    if xs[i]>0:
        for j in range (xs[i]):
            print ('x', end='')
        print ('\n')
    else:
        print ('\n')
