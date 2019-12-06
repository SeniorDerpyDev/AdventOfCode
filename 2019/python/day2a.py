with open('../day_2.txt', 'r') as f:
    p = [int(s) for s in f.read().rstrip().split(',')]

p[1] = 12
p[2] = 2
ip = 0
while p[ip] != 99:
    op, a, b, r = p[ip : ip+4]
    if op == 1:
        p[r] = p[a] + p[b]
    elif op == 2:
        p[r] = p[a] * p[b]
    ip += 4

print(p[0])
