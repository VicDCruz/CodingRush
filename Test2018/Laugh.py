n = int(raw_input())
laughs = []
for x in range(0, n):
    laughs.append(int(raw_input()))
for laugh in laughs:
    output = ""
    for x in range(0, laugh):
        output = output + 'w'
    print output
