n = int(raw_input())
books = {}
for x in range(0, n):
    book = raw_input()
    available = raw_input()
    books[book] = available
bookToCheck = raw_input()
if bookToCheck in books.keys():
    print books[bookToCheck]
else:
    print "El libro no existe"
