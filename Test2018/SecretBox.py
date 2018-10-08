n = int(raw_input())
boxOut = int(raw_input())
boxes = []
for x in range(0, n):
    number = int(raw_input())
    if number != boxOut:
        boxes.append(number)
for box in boxes:
    print box
