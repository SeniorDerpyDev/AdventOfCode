from functools import reduce
from operator import mul

with open('../day_3.txt', 'r') as f:
    trees = list(line.rstrip() for line in f)

Y = len(trees)
X = len(trees[0])

def countTrees(slope):
    dx, dy = slope
    x, y = 0, 0
    count = 0
    while y < Y:
        if trees[y][x] == '#':
            count += 1
        x = (x + dx) % X
        y += dy
    return count

p1 = countTrees((3, 1))
p2 = reduce(mul, map(countTrees, [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]), 1)

print('part 1:', p1)
print('part 2:', p2)

