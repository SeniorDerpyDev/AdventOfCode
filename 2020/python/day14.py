def parse(s):
    l, r = s.split(' = ')
    if l == "mask":
        return r
    return int(l[4:-1]), int(r)

def get_p2_masks(mask):
    mask = mask.replace('0', '_')
    l = [mask]
    i = mask.find('X', 0)
    while i != -1:
        l = [m[:i] + '1' + m[i+1:] for m in l] + [m[:i] + '0' + m[i+1:] for m in l]
        i = mask.find('X', i+1)
    return [m.replace('_', 'X') for m in l]


with open('../day_14.txt', 'r') as f:
    pgm = [parse(line) for line in f]

mem = {}
for inst in pgm:
    if type(inst) == str:
        or_mask, and_mask = int(inst.replace('X', '0'), 2), int(inst.replace('X', '1'), 2)
    else:
        addr, v = inst
        mem[addr] = (v & and_mask) | or_mask
print('part 1:', sum(mem.values()))

mem = {}
for inst in pgm:
    if type(inst) == str:
        masks = get_p2_masks(inst)
    else:
        addr, v = inst
        for m in masks:
            or_mask, and_mask = int(m.replace('X', '0'), 2), int(m.replace('X', '1'), 2)
            mem[(addr & and_mask) | or_mask] = v
print('part 2:', sum(mem.values()))

