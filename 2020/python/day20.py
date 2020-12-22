from collections import defaultdict, deque
from math import sqrt

# http://mathonline.wikidot.com/the-group-of-symmetries-of-the-square
def rotate_left(t):
    return transpose1(flip_horizontal(t))

def rotate_right(t):
    return [list(r) for r in zip(*t[::-1])]

def rotate_180(t):
    return rotate_right(rotate_right(t))

def flip_vertical(t):
    return t[::-1]

def flip_horizontal(t):
    return [r[::-1] for r in t]

def transpose1(t):
    return [list(r) for r in zip(*t)]

def transpose2(t):
    return rotate_right(flip_horizontal(t))


def get_top(t):
    return ''.join(t[0])

def get_bottom(t):
    return ''.join(t[-1])

def get_left(t):
    return ''.join([r[0] for r in t])

def get_right(t):
    return ''.join([r[-1] for r in t])

transformations = [lambda t: t, rotate_left, rotate_right, rotate_180, flip_vertical, flip_horizontal, transpose1, transpose2]

tiles = {}
with open('../day_20.txt') as f:
    tile = []
    for line in f:
        if line.startswith('Tile'):
            n = int(line[5:9])
        elif line == '\n':
            tiles[n] = tile
            tile = []
        else:
            tile.append(list(line.rstrip()))

GRID_SIZE = int(sqrt(len(tiles)))

tops = defaultdict(set) 
lefts = defaultdict(set) 
tiles_trf = {}
for t_id, tile in tiles.items():
    for i, trf in enumerate(transformations):
        tt = trf(tile)
        tops[get_top(tt)].add((t_id, i))
        lefts[get_left(tt)].add((t_id, i))
        tiles_trf[t_id, i] = tt

grid = {}

def find_image(x, y):
    if y == GRID_SIZE:
        return True

    used_ids = {t[0] for t in grid.values()}
    available = tiles_trf.keys()
    if x > 0:
        left_tile = tiles_trf[grid[x-1, y]]
        available &= lefts[get_right(left_tile)]
    if y > 0:
        top_tile = tiles_trf[grid[x,y-1]]
        available &= tops[get_bottom(top_tile)]

    n_x, n_y = x + 1, y
    if n_x == GRID_SIZE:
        n_x, n_y = 0, y + 1

    for t in available:
        if not t[0] in used_ids:
            grid[x,y] = t
            if find_image(n_x, n_y):
                return True
            del grid[x,y]

find_image(0, 0)
print('part 1:', grid[0, 0][0] * grid[0, GRID_SIZE-1][0] * grid[GRID_SIZE-1, 0][0] * grid[GRID_SIZE-1, GRID_SIZE-1][0])


image = []
for y in range(GRID_SIZE):
    for i in range(1, 9):
        s = ''.join(c for x in range(GRID_SIZE) for c in tiles_trf[grid[x, y]][i][1:-1])
        image.append(s)

monster = [ "                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]
monster = [(i,j) for j, m in enumerate(monster) for i, c in enumerate(m) if c == '#']

for trf in transformations:
    img = trf(image)
    count = 0
    for y in range(0, GRID_SIZE*8 - 3):
        for x in range(0, GRID_SIZE*8 - 20):
            if all(img[y+j][x+i] == '#' for i, j in monster):
                count += 1
    if count > 0:
        print('part 2:', sum(c == '#' for row in img for c in row) - count*len(monster))
        break

