s = raw_input()
if s != "":
    name = "miguel"
    newString = s
    output = []
    for character in name:
        newString = s.replace(character, '')
        diffString = len(s) - len(newString)
        output.append(diffString)
    print min(output)
else:
    print 0
