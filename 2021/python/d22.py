from math import prod
import re

def difference(c1, c2):
    overlap = []
    for i in [0, 2, 4]:
        if c1[i+1] >= c2[i] and c1[i] <= c2[i+1]:
            overlap += [max(c1[i], c2[i]), min(c1[i+1], c2[i+1])]
        else:
            return [c1]
    new_cuboids = []
    if c1[0] != overlap[0]:
        new_cuboids.append([c1[0], overlap[0]-1, *c1[2:]])
    if c1[1] != overlap[1]:
        new_cuboids.append([overlap[1]+1, c1[1], *c1[2:]])
    if c1[2] != overlap[2]:
        new_cuboids.append([*overlap[:2], c1[2], overlap[2]-1, *c1[4:]])
    if c1[3] != overlap[3]:
        new_cuboids.append([*overlap[:2], overlap[3]+1, c1[3], *c1[4:]])
    if c1[4] != overlap[4]:
        new_cuboids.append([*overlap[:4], c1[4], overlap[4]-1])
    if c1[5] != overlap[5]:
        new_cuboids.append([*overlap[:4], overlap[5]+1, c1[5]])
    return new_cuboids

with open('../day_22.txt') as f:
    instructions = [(re.search('(on|off)', l).group(), [int(n.group()) for n in re.finditer('-?\d+', l)]) for l in f]

cuboids = []
for action, cuboid in instructions:
    new_cuboids = [cuboid] if action == 'on' else []
    for c in cuboids:
        new_cuboids += difference(c, cuboid)
    cuboids = new_cuboids

print('part 1:', sum(prod(c[i+1] - c[i] + 1 for i in [0, 2, 4]) for c in cuboids if -50 <= c[0] <= 50))
print('part 2:', sum(prod(c[i+1] - c[i] + 1 for i in [0, 2, 4]) for c in cuboids))
