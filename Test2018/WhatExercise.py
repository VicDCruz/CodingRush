n = int(raw_input())
exercises = []
for x in range(0, n):
    exercises.append(int(raw_input()))
odd = 0
even = 0
for x in range(0, n):
    if x % 2 == 0:
        even = even + exercises[x]
    else:
        odd = odd + exercises[x]
if odd < even:
    print 'P'
else:
    print 'I'
