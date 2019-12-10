from math import (pi, atan2, gcd)
from itertools import (repeat, product)

def dir_sort_f(d):
    x, y = d
    r = atan2(y, x)
    if (r < -pi/2):
        r += 2*pi
    return r

def scan(asteroid):
    directions = set()
    x0, y0 = asteroid
    for y,x in product(range(h), range(w)):
        if (x, y) == (x0, y0):
            continue
        d = gcd(y - y0, x - x0)
        dx, dy = (x - x0) // d, (y - y0) // d
        directions.add((dx, dy))

    visible = []
    for (dx,dy) in sorted(directions, key=dir_sort_f):
        xi, yi = x0 + dx, y0 + dy
        while xi >= 0 and xi < w and yi >= 0 and yi < h:
            if asteroid_map[yi][xi]:
                visible.append((xi, yi))
                break
            xi += dx
            yi += dy
    return visible


with open('../day_10.txt', 'r') as f:
    m = [[c == '#' for c in line.strip()] for line in f.read().splitlines()]

asteroid_map, w, h = m, len(m[0]), len(m)

best_asteroid = None
best_score = 0
for y,x in product(range(h), range(w)):
    if not asteroid_map[y][x]:
        continue
    score = len(scan((x,y)))
    if score > best_score:
        best_asteroid = (x,y)
        best_score = score

print('part 1:', best_score)

targets = scan(best_asteroid)
x200, y200 = targets[199]
print('part 2:', x200*100 + y200)
