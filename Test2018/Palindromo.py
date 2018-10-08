n = int(raw_input())
if n >= 0:
    words = []
    for i in range(0, n):
        words.append(raw_input())
    for word in words:
        length = len(word)
        cont = 0
        sameLetter = True
        while cont < length and sameLetter:
            sameLetter = word[cont] == word[length - cont - 1]
            cont = cont + 1
        if sameLetter:
            print "P"
        else:
            print "NP"
else:
    print "Error: Numero negativo"
