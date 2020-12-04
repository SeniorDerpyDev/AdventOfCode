from itertools import count
from functools import reduce
from operator import mul

with open('../day_3.txt', 'r') as f:
    terrain = list(line.rstrip() for line in f)

def countTrees(slope):
    dx, dy = slope
    return sum(1 for row, x in zip(terrain[::dy], count(0, dx)) if row[x % len(row)] == '#')

p1 = countTrees((3, 1))
p2 = reduce(mul, map(countTrees, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]), 1)

print('part 1:', p1)
print('part 2:', p2)

