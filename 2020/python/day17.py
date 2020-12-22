from itertools import product

with open('../day_17.txt', 'r') as f:
    initial_grid = {(x,y) for y, line in enumerate(f) for x, c in enumerate(line.strip()) if c == '#'}

def simulation(grid, dimensions):
    neighbors = list(product([-1, 0, 1], repeat=dimensions))

    def get_neighbors(cube):
        return {tuple(a+b for a, b in zip(cube, nbor)) for nbor in neighbors}

    for _ in range(6):
        cubes_to_process = set()
        for cube in grid:
            cubes_to_process |= get_neighbors(cube)

        next_grid = set() 
        for cube in cubes_to_process:
            count = sum(c in grid for c in get_neighbors(cube) if c != cube)
            if count == 3 or (count == 2 and cube in grid):
                next_grid.add(cube)
        grid = next_grid
    return len(grid)

print("part 1 ", simulation({(x,y,0) for x,y in initial_grid}, 3))
print("part 2 ", simulation({(x,y,0,0) for x,y in initial_grid}, 4))
