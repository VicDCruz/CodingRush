n = int(raw_input())
words = []
for x in range(0, n):
    words.append(raw_input())
distance = n / 2
output = ""
for cont in range(0, n):
    newPosition = distance + cont
    if newPosition > n - 1:
        newPosition = distance + cont - n
    output += words[newPosition] + " "
print output
