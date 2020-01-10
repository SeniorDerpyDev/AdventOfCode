from collections import defaultdict
from math import ceil

def parse(s):
    q, m = s.split()
    return (int(q), m)

def parse_equations(lines):
    e = {'ORE': (1, [])}
    for line in lines:
        left, right = line.rstrip().split(' => ')
        amount, mat = parse(right)
        e[mat] = (amount, [parse(s) for s in left.split(', ')])
    return e

def topologicalSort(equations): 
    visited = defaultdict(bool) 
    stack = []

    def topologicalSortUtil(e): 
        visited[e] = True
        for (_, m) in equations[e][1]: 
            if visited[m] == False: 
                topologicalSortUtil(m) 
        stack.insert(0, e)

    for e in equations:
        if visited[e] == False: 
            topologicalSortUtil(e)
    return stack

def calc_ore_amount(amount):
    wanted = defaultdict(int, {'FUEL': amount})
    
    for material in topologicalSort(equations):
        quantity = wanted[material]
        produced, inputs = equations[material]
        mult = ceil(quantity / produced)
        for n, mat in inputs:
            wanted[mat] += mult * n

    return wanted['ORE']


with open('../day_14.txt') as f:
    equations = parse_equations(f.readlines())

ore = calc_ore_amount(1)
print('part 1:', ore)


min_fuel = 10**12 // ore
max_fuel = 3281820

while min_fuel < max_fuel:
    fuel = (max_fuel + min_fuel) // 2 + 1
    ore = calc_ore_amount(fuel)
    if ore > 10**12:
        max_fuel = fuel - 1
    else:
        min_fuel = fuel
print('part 2:', max_fuel)

