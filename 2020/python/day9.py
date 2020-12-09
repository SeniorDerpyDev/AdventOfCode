from itertools import combinations

with open('../day_9.txt', 'r') as f:
    numbers = list(int(s.rstrip()) for s in f)

p1 = next(n for i, n in enumerate(numbers[25:], 25) if all(n1+n2 != n for n1,n2 in combinations(numbers[i-25:i], 2)))

b, e, acc = 0, 1, numbers[0]
while acc != p1:
    if acc < p1:
        acc += numbers[e]
        e += 1
    else:
        acc -= numbers[b]
        b += 1
p2 = max(numbers[b:e]) + min(numbers[b:e])

print('part 1:', p1)
print('part 2:', p2)
