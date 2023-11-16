R = [(0, 0)] * 10
T1 = set()
T2 = set()
for l in open(0):
    d, n = l.strip().split()
    for _ in range(int(n)):
        x, y = R[0]
        R[0] = {'U': (x, y+1), 'D': (x, y-1), 'L': (x-1, y), 'R': (x+1, y)}[d]
        for i in range(1, 10):
            hx, hy = R[i-1]
            tx, ty = R[i]
            if abs(hx-tx) == 2 or abs(hy-ty) == 2:
                tx += 1 if hx > tx else -1 if hx < tx else 0
                ty += 1 if hy > ty else -1 if hy < ty else 0
            R[i] = tx, ty
            if i == 1:
                T1.add(R[i])
            elif i == 9:
                T2.add(R[i])

print(len(T1))
print(len(T2))
