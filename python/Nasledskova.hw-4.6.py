word=input()
l=len(word)
while l>0:
    word=list(word)
    x=word.pop(0)
    print (''.join(word))
    l=len(word)
