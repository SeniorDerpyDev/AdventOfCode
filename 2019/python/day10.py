from math import atan2, gcd

def key(d):
    x, y = d
    return -atan2(x, y)

def scan(asteroid):
    x0, y0 = asteroid
    directions = [(x - x0, y - y0) for y in range(h) for x in range(w) if gcd(x - x0, y - y0) == 1]

    visible = []
    for dx, dy in sorted(directions, key=key):
        xi, yi = x0 + dx, y0 + dy
        while xi >= 0 and xi < w and yi >= 0 and yi < h:
            if asteroid_map[yi][xi]:
                visible.append((xi, yi))
                break
            xi += dx
            yi += dy
    return visible


with open('../day_10.txt', 'r') as f:
    asteroid_map = [[c == '#' for c in line.strip()] for line in f.read().splitlines()]

w, h = len(asteroid_map[0]), len(asteroid_map)

best = max((scan((x, y)) for y in range(h) for x in range(w) if asteroid_map[y][x]), key=len)
print('part 1:', len(best))

x200, y200 = best[199]
print('part 2:', x200 * 100 + y200)
