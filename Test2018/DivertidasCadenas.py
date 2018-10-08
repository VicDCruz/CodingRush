n = int(raw_input())
if n >= 0:
    words = []
    for x in range(0, n):
        words.append(raw_input())
    for word in words:
        output = 0
        cont = 1
        baseLetter = word[0]
        while cont < len(word):
            if baseLetter == word[cont]:
                areEqual = True
                output = output + 1
            elif baseLetter != word[cont]:
                baseLetter = word[cont]
            cont = cont +1
        print output
else:
    print "Error: Numero fuera de rango"
