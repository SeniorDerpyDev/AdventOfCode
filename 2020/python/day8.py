with open('../day_8.txt', 'r') as f:
    pgm = [(op, int(n)) for op, n in (line.split() for line in f)]

def run(pgm):
    ip, acc = 0, 0
    executed = set()
    while ip not in executed and ip < len(pgm):
        executed.add(ip)
        op, arg = pgm[ip]
        if op == 'acc':
            acc += arg
            ip += 1
        elif op == 'jmp':
            ip += arg
        else:
            ip += 1
    return acc, ip == len(pgm)


def run_all(pgm):
    for i, (op, arg) in enumerate(pgm):
        if op == 'acc':
            continue

        fixed = list(pgm)
        fixed[i] = ('nop', arg) if op == 'jmp' else ['jmp', arg]
        acc, finished = run(fixed)
        if finished:
            return acc

p1 = run(pgm)[0]
p2 = run_all(pgm)

print('part 1:', p1)
print('part 2:', p2)
