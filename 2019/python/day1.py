def calc_fuel(n):
    n = n // 3 - 2
    if n <= 0:
        return 0
    return n + calc_fuel(n)

with open('../day_1.txt', 'r') as f:
    l = list(int(s.rstrip()) for s in f)

print('result 1:', sum(n//3-2 for n in l))
print('result 2:', sum(calc_fuel(n) for n in l))
