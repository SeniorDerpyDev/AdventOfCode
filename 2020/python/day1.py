from itertools import combinations

with open('../day_1.txt', 'r') as f:
    expenses = list(int(s.rstrip()) for s in f)

lookup = set(expenses)

p1 = next(n*(2020-n) for n in expenses if 2020-n in lookup)
p2 = next(l[0]*l[1]*l[2] for l in combinations(expenses, 3) if sum(l) == 2020) 

print('part 1:', p1)
print('part 1:', p2)
