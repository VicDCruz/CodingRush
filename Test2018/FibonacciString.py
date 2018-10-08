wordOne = raw_input()
wordTwo = raw_input()
n = int(raw_input())

if n <= 15 and n >= 1:
    output = ""
    for x in range(0, n):
        if x == 0:
            output = wordOne
        elif x == 1:
            output = wordTwo
        else:
            output = wordOne + wordTwo
            wordOne = wordTwo
            wordTwo = output
    print output
else:
    print "Error: Numero fuera de rango"
