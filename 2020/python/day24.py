from collections import Counter

def translate(s):
    i, p = 0, 0
    while i < len(s):
        if s[i] == 'n' or s[i] == 's':
            p += directions[s[i:i+2]]
            i += 2
        else:
            p += directions[s[i]]
            i += 1
    return p

def get_neighbors(tile):
    return (tile + d for d in directions.values())

# https://www.redblobgames.com/grids/hexagons/
directions = {'e': 2, 'w': -2, 'ne': 1+1j, 'nw': -1+1j, 'se': 1-1j, 'sw': -1-1j }

with open('../day_24.txt') as f:
    tile_count = Counter(translate(line.rstrip()) for line in f)
    black_tiles = set(t for t, c in tile_count.items() if c % 2 == 1)

print('part 1:', len(black_tiles))

for _ in range(100):
    neighbors = Counter(n_tile for tile in black_tiles for n_tile in get_neighbors(tile))
    black_tiles = {t for t, c in neighbors.items() if c == 2 or (t in black_tiles and c == 1)}

print('part 2:', len(black_tiles))

