p1 = p2 = 0
for l in open(0):
    a,b = l.strip().split()
    a = ord(a) - ord('A')
    b = ord(b) - ord('X')

    p1 += b + 1
    if (b-a) % 3 == 1:
        p1 += 6
    elif b == a:
        p1 += 3

    if b == 0:
        p2 += (a-1) % 3 + 1
    elif b == 1:
        p2 += 3 + a + 1
    else:
        p2 += 6 + (a+1) % 3 + 1

print(p1)
print(p2)

