movements = {'R': (1,0), 'L': (-1,0), 'U': (0,1), 'D': (0,-1)}

def turtle(steps):
    x, y = 0, 0
    points = set()
    for s in steps:
        dx, dy = movements[s[0]]
        d = int(s[1:])
        for _ in range(d):
            x += dx
            y += dy
            points.add((x,y))
    return points

with open('../day_3.txt') as f:
    wire1 = f.readline().rstrip().split(',')
    wire2 = f.readline().rstrip().split(',')

crossings = turtle(wire1) & turtle(wire2)
result = min((abs(x)+abs(y) for (x,y) in crossings))
print(result)
