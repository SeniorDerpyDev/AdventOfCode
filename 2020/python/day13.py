with open('../day_13.txt', 'r') as f:
    lines = f.read().splitlines()

timestamp = int(lines[0])
buses = [(i, int(s)) for i, s in enumerate(lines[1].split(',')) if s != 'x']

bus, dist = min(((n, n - timestamp % n) for _, n in buses), key = lambda t: t[1])
print('part 1:', bus * dist)

_, step = buses[0]
n = step
for i, m in buses[1:]:
    r = -i % m
    while n % m != r:
        n += step
    step *= m
print('part 2:', n)

