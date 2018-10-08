n = int(raw_input())
if n >= 0:
    faces = []
    for x in range(0, n):
        face = int(raw_input())
        if face <= 0:
            print "Error: Numero fuera de rango"
            break
        faces.append(face)
    for face in faces:
        if face == 1:
            print 1
        else:
            print face * face * face - (face - 2) * (face - 2) * (face - 2)
else:
    print "Error: Numero fuera de rango"
