with open('../day_1.txt', 'r') as f:
    expenses = list(int(s.rstrip()) for s in f)

target = 2020
lookup = set(expenses)
p1 = next(n*(target-n) for n in expenses if target-n in lookup)
p2 = next(n*m*(target-n-m) for i,n in enumerate(expenses) for m in expenses[i+1:] if target-n-m in lookup)

print('part 1:', p1)
print('part 2:', p2)
