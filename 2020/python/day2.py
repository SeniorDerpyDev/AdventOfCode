def parse(s):
    [r, c, pwd] = s.split()
    low, high = map(int, r.split('-'))
    return (low, high, c[0], pwd)

with open('../day_2.txt', 'r') as f:
    passwords = list(parse(line.rstrip()) for line in f)

p1 = sum(1 for low, high, c, pwd in passwords if low <= pwd.count(c) <= high)
p2 = sum(1 for low, high, c, pwd in passwords if (pwd[low-1] == c) != (pwd[high-1] == c))

print('part 1:', p1)
print('part 2:', p2)
