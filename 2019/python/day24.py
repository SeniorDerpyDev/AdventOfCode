masks = {
    1<<0  : (        1<<1  | 1<<5         , 1<<7 | 1<<11 , 0),
    1<<1  : (1<<0  | 1<<2  | 1<<6         , 1<<7         , 0),
    1<<2  : (1<<1  | 1<<3  | 1<<7         , 1<<7         , 0),
    1<<3  : (1<<2  | 1<<4  | 1<<8         , 1<<7         , 0),
    1<<4  : (1<<3          | 1<<9         , 1<<7 | 1<<13 , 0),

    1<<5  : (        1<<6  | 1<<10 | 1<<0 , 1<<11        , 0),
    1<<6  : (1<<5  | 1<<7  | 1<<11 | 1<<1 , 0            , 0),
    1<<7  : (1<<6  | 1<<8  | 1<<12 | 1<<2 , 0            , 1<<0 | 1<<1 | 1<<2 | 1<<3 | 1<<4),
    1<<8  : (1<<7  | 1<<9  | 1<<13 | 1<<3 , 0            , 0),
    1<<9  : (1<<8          | 1<<14 | 1<<4 , 1<<13        , 0),

    1<<10 : (        1<<11 | 1<<15 | 1<<5 , 1<<11        , 0),
    1<<11 : (1<<10 | 1<<12 | 1<<16 | 1<<6 , 0            , 1<<0 | 1<<5 | 1<<10 | 1<<15 | 1<<20),
    1<<12 : (1<<11 | 1<<13 | 1<<17 | 1<<7 , 0            , 0),
    1<<13 : (1<<12 | 1<<14 | 1<<18 | 1<<8 , 0            , 1<<4 | 1<<9 | 1<<14 | 1<<19 | 1<<24),
    1<<14 : (1<<13         | 1<<19 | 1<<9 , 1<<13        , 0),

    1<<15 : (        1<<16 | 1<<20 | 1<<10, 1<<11        , 0),
    1<<16 : (1<<15 | 1<<17 | 1<<21 | 1<<11, 0            , 0),
    1<<17 : (1<<16 | 1<<18 | 1<<22 | 1<<12, 0            , 1<<20 | 1<<21 | 1<<22 | 1<<23 | 1<<24),
    1<<18 : (1<<17 | 1<<19 | 1<<23 | 1<<13, 0            , 0),
    1<<19 : (1<<18         | 1<<24 | 1<<14, 1<<13        , 0),

    1<<20 : (        1<<21         | 1<<15, 1<<17 | 1<<11, 0),
    1<<21 : (1<<20 | 1<<22         | 1<<16, 1<<17        , 0),
    1<<22 : (1<<21 | 1<<23         | 1<<17, 1<<17        , 0),
    1<<23 : (1<<22 | 1<<24         | 1<<18, 1<<17        , 0),
    1<<24 : (1<<23                 | 1<<19, 1<<17 | 1<<13, 0),
}

def read_biome(s):
    s = s.translate({ ord('.'): '0', ord('#'): '1', ord('\n'): '' })
    return int(s[::-1], 2)

def count_bugs(biome):
    return bin(biome).count('1')

def next_generation(biome):
    r = 0
    bit = 1 
    for _ in range(25):
        mask = masks[bit][0]
        adjacent = count_bugs(biome & mask)
        bug = biome & bit
        if bug and adjacent == 1:
            r = r | bit
        if not bug and 0 < adjacent < 3:
            r = r | bit
        bit = bit << 1
    return r

def next_generation2(biome, outer, inner):
    r = 0
    bit = 1 
    for i in range(25):
        if i == 12:
            bit = bit << 1
            continue

        mask = masks[bit]
        adjacent = count_bugs(biome & mask[0]) + count_bugs(outer & mask[1]) + count_bugs(inner & mask[2])
        bug = biome & bit
        if bug and adjacent == 1:
            r = r | bit
        if not bug and 0 < adjacent < 3:
            r = r | bit
        bit = bit << 1
    return r


with open('../day_24.txt', 'r') as f:
    initial_biome = read_biome(f.read())

biomes = set()
biome = initial_biome
while biome not in biomes:
    biomes.add(biome)
    biome = next_generation(biome)

print('part 1:', biome)


biomes = [initial_biome]
for _ in range(200):
    biomes.insert(0, 0)
    biomes.append(0)

    start = next_generation2(biomes[0], 0, biomes[1])
    end = next_generation2(biomes[-1], biomes[-2], 0)
    biomes = [next_generation2(biome, outer, inner) for outer, biome, inner in zip(biomes, biomes[1:], biomes[2:])]
    
    if start:
        biomes.insert(0, start)
    if end:
        biomes.append(end)

print('part 2:', sum(count_bugs(b) for b in biomes if b))
