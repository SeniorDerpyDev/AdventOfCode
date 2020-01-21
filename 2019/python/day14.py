from collections import defaultdict
from math import ceil

def parse(s):
    q, m = s.split()
    return (int(q), m)

def parse_equations(lines):
    e = {}
    for line in lines:
        left, right = line.rstrip().split(' => ')
        amount, mat = parse(right)
        e[mat] = (amount, [parse(s) for s in left.split(', ')])
    return e

def calc_ore_amount(amount):
    inventory = defaultdict(int, {'FUEL': -amount})
    work = ['FUEL']
    while work:
        material = work.pop(0)
        quantity = -inventory[material]
        produced, inputs = equations[material]
        mult = ceil(quantity / produced)
        inventory[material] += mult * produced
        for n, mat in inputs:
            inventory[mat] -= mult * n
            if inventory[mat] < 0 and mat != 'ORE':
                work.append(mat)

    return -inventory['ORE']


with open('../day_14.txt') as f:
    equations = parse_equations(f.readlines())
ore = calc_ore_amount(1)
print('part 1:', ore)


min_fuel = 10**12 // ore
max_fuel = 2 * min_fuel

while min_fuel < max_fuel:
    fuel = (max_fuel + min_fuel) // 2 + 1
    ore = calc_ore_amount(fuel)
    if ore > 10**12:
        max_fuel = fuel - 1
    else:
        min_fuel = fuel
print('part 2:', max_fuel)

