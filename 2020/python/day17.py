from collections import Counter
from itertools import product

with open('../day_17.txt', 'r') as f:
    initial_grid = {(x,y) for y, line in enumerate(f) for x, c in enumerate(line.strip()) if c == '#'}

def simulation(grid, dimensions):
    directions = list(product([-1, 0, 1], repeat=dimensions))
    zero = (0,) * dimensions

    def get_neighbors(cube):
        return (tuple(a+b for a, b in zip(cube, d)) for d in directions if d != zero)

    for _ in range(6):
        neighbors = Counter(n_cube for cube in grid for n_cube in get_neighbors(cube))
        grid = {cube for cube, c in neighbors.items() if c == 3 or (cube in grid and c == 2)}
    return len(grid)

print("part 1 ", simulation({(x,y,0) for x,y in initial_grid}, 3))
print("part 2 ", simulation({(x,y,0,0) for x,y in initial_grid}, 4))
