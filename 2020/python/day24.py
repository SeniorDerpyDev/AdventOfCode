moves = {'e': (1,-1,0), 'w': (-1,1,0), 'ne': (1,0,-1), 'nw': (0,1,-1), 'se': (0,-1,1), 'sw': (-1,0,1) }

def translate(s):
    x, y, z = 0, 0, 0
    i = 0
    while i < len(s):
        if s[i] == 'n' or s[i] == 's':
            mov = moves[s[i:i+2]]
            i += 2
        else:
            mov = moves[s[i]]
            i += 1
        x += mov[0]
        y += mov[1]
        z += mov[2]
    return (x, y, z)

def get_neighbors(tile):
    x, y, z = tile
    return {(x+i, y+j, z+k) for i,j,k in moves.values()}

black_tiles = set()
with open('../day_24.txt') as f:
    for line in f:
        tile = translate(line.rstrip())
        if tile in black_tiles:
            black_tiles.remove(tile)
        else:
            black_tiles.add(tile)

print('part 1:', len(black_tiles))


for _ in range(100):
    next_black_tiles = set()
    white_tiles_to_flip = set()
    for tile in black_tiles:
        neighbors = get_neighbors(tile)
        if 0 < len(black_tiles & neighbors) < 3:
            next_black_tiles.add(tile)
        for white_tile in neighbors - black_tiles:
            if 2 == len(black_tiles & get_neighbors(white_tile)):
                white_tiles_to_flip.add(white_tile)
    black_tiles = next_black_tiles | white_tiles_to_flip

print('part 2:', len(black_tiles))

