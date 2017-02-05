import re

def search (text):
    otr = re.search ('<tr valign="top">\n<td align="right">Отряд:</td>\n<td align="left"><a href="(.+?)" title="(.+?)">(.+?)</a></td>\n</tr>', text)
    if otr:
        result = otr.group(3)
    return result

def main ():
    f = open('file_10.6.html', 'r', encoding = 'utf8')
    file = f.read()
    f.close()
    ans = search (file)
    print (ans)

main()
