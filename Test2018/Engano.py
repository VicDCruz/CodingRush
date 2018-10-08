n = int(raw_input())

if n <= 100:
    cards = []
    for x in range(0, n):
        cards.append(int(raw_input()))
    newOrder = []
    for x in range(0, n):
        newOrder.append(int(raw_input()))
    for x in newOrder:
        print cards[x]
else:
    print "Error: Numero fuera de rango"
