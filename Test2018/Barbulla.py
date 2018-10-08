n = int(raw_input())

if n <= 1000 and n >= 1:
    output = 0
    for x in range(1, n + 1):
        output = output + (x * (x + 1) / 2)
    print output
else:
    print "Error: Numero fuera de rango"
