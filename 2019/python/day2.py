def run(pgm, noun, verb):
    p = list(pgm)
    p[1] = noun
    p[2] = verb
    ip = 0
    while p[ip] != 99:
        op, a, b, r = p[ip : ip+4]
        if op == 1:
            p[r] = p[a] + p[b]
        elif op == 2:
            p[r] = p[a] * p[b]
        ip += 4

    return p[0]

with open('../day_2.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

print('part 1:', run(pgm, 12, 2))

r = next(n*100+v for n in range(100) for v in range(100) if run(pgm, n, v) == 19690720)
print('part 2:', r)
