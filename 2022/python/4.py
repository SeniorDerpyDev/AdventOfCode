import re
p1 = p2 = 0
for l in open(0):
    b1,e1,b2,e2 = (int(f) for f in re.findall("\d+", l))
    if b1<=b2<=e2<=e1 or b2<=b1<=e1<=e2:
        p1 += 1
    if not (e1<b2 or e2<b1):
        p2 += 1
print(p1)
print(p2)

