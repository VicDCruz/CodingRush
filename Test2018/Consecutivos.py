n = int(raw_input())
numbers = raw_input().split(' ')
numbers.sort()
cont = 0
isConsecutive = True
while cont < len(numbers) - 1 and isConsecutive:
    isConsecutive = (int(numbers[cont + 1]) - int(numbers[cont])) == 1
    cont = cont + 1
if isConsecutive:
    print 'SI'
else:
    print 'NO'
