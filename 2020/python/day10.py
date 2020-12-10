from itertools import groupby
from functools import reduce

with open('../day_10.txt', 'r') as f:
    jolts = [0] + sorted(int(s.rstrip()) for s in f)

deltas = [m-n for n, m in zip(jolts, jolts[1:])]

p1 = sum(1 for d in deltas if d==1) * (1 + sum(1 for d in deltas if d==3))

tr = {4: 7, 3: 4, 2: 2, 1: 1}
p2 = reduce(lambda acc, n: acc * tr[n], (sum(1 for _ in g) for d, g in groupby(deltas) if d == 1), 1)

print("part 1:", p1)
print("part 2:", p2)

