movements = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}

def turtle(steps):
    x, y, n = 0, 0, 0
    points = dict()
    for s in steps:
        dx, dy = movements[s[0]]
        d = int(s[1:])
        for _ in range(d):
            x += dx
            y += dy
            n += 1
            if (x,y) not in points:
                points[(x,y)] = n
    return points

with open('../day_3.txt') as f:
    wire1 = f.readline().rstrip().split(',')
    wire2 = f.readline().rstrip().split(',')

d1 = turtle(wire1)
d2 = turtle(wire2)
crossings = d1.keys() & d2.keys()
result = min(d1[p] + d2[p] for p in crossings)
print(result)
