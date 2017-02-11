import re

def buka ():
    f = open('file_11.6.html', 'r', encoding = 'utf8')
    file = f.read()
    f.close()
    return file

def berubah (file):
    new = re.sub(u'Ф[иИ][нН][лЛ][Яя]́?[Нн][Дд][Ии](.+?[ ")<,.»/?!])', u'Малайзи\\1', file)
    return new

def baru (s):
    f = open('file_11.6.2.html', 'w', encoding = 'utf8')
    f.write(s)
    f.close
    
def main ():
    text = buka()
    art = berubah(text)
    baru (art)

main ()
