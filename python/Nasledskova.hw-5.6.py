capital='АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
s=0
cap=0
f=open('file_5.6.txt', 'r', encoding='utf8')
file=f.readlines()
l=len(file)
for i in range (0, l):
    file[i]=file[i].split(' ')
for i in range (0, l):
    m=len(file[i])
    for j in range (0, m):
        if file[i][j][0] in capital:
           cap+=1
        s+=1
print ((cap/s)*100)
f.close()
