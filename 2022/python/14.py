rocks = set()
LIM = 0
for line in open(0):
    L = [[int(n) for n in p.split(',')] for p in line.strip().split(' -> ')]
    for [x1, y1], [x2, y2] in zip(L, L[1:]):
        x1, x2 = sorted([x1, x2])
        y1, y2 = sorted([y1, y2])
        LIM = max(LIM, y2)
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                rocks.add(x + y*1j)
LIM += 1

rocks1 = rocks.copy()
s = 500
while True:
    if s.imag >= LIM:
        break
    for ds in (1j, -1 + 1j, 1 + 1j):
        if (s + ds) not in rocks1:
            s += ds
            break
    else:
        rocks1.add(s)
        s = 500
print(len(rocks1) - len(rocks))

rocks2 = rocks.copy()
s = 500
while 500 not in rocks2:
    if s.imag < LIM:
        for ds in (1j, -1 + 1j, 1 + 1j):
            if (s + ds) not in rocks2:
                s += ds
                break
        else:
            rocks2.add(s)
            s = 500
    else:
        rocks2.add(s)
        s = 500
print(len(rocks2) - len(rocks))
