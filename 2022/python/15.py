import re
B = set()
S = {}
for line in open(0):
    sx, sy, bx, by = (int(s) for s in re.findall("-?\d+", line))
    B.add((bx,by))
    S[(sx, sy)] = abs(bx-sx) + abs(by-sy)

Y = 2_000_000
R = set()
for (sx, sy), d in S.items():
    dx = d - abs(Y - sy)
    if dx >= 0:
        R.update(range(sx - dx, sx + dx + 1))
print(len(R) - sum(y == Y for _,y in B))

L = 4_000_000
for (X, Y), D in S.items():
    dx, dy = 1, 1
    x, y = X, Y - D - 1
    ans = 0
    seg = 0
    while seg < 4:
        if 0<=x<=L and 0<=y<=L and all(abs(x-x1) + abs(y-y1) > d1 for (x1, y1), d1 in S.items()):
            ans = x*L + y
            break
        x += dx
        y += dy
        if x == X: dy = -dy; seg += 1
        if y == Y: dx = -dx; seg += 1
    if ans:
        print(ans)
        break
