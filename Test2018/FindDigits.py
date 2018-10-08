import re
n = int(raw_input())
sentences = []
numbers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for x in range(0, n):
    sentences.append(raw_input())
for sentence in sentences:
    number = re.sub(r"[A-Za-z ,!%&]", "", sentence)
    for n in number:
        numbers[int(n)] = numbers[int(n)] + 1
cont = 0
for n in numbers:
    print "El " + str(cont) + " aparece " + str(n) + " veces."
    cont = cont + 1
