import itertools

R, W = 0, 1

parms = {
    1: (R, R, W), 2: (R, R, W), 3: (W,), 4: (R,),
    5: (R, R), 6: (R, R), 7: (R, R, W), 8: (R, R, W)
}

def run_program(pgm, inputs):
    p = list(pgm)
    ip = 0
    while p[ip] != 99:
        modes, opcode = divmod(p[ip], 100)
        ip += 1

        args = [0, 0, 0]
        for n, rw in enumerate(parms[opcode]):
            val, ip = p[ip], ip + 1
            modes, m = divmod(modes, 10)
            if rw == R and m == 0:
                val = p[val]
            args[n] = val

        a, b, c = args
        if opcode == 1:
            p[c] = a + b
        elif opcode == 2:
            p[c] = a * b
        elif opcode == 3:
            p[a] = next(inputs)
        elif opcode == 4:
            yield a
        elif opcode == 5:
            if a != 0:
                ip = b
        elif opcode == 6:
            if a == 0:
                ip = b
        elif opcode == 7:
            p[c] = 1 if a < b else 0
        elif opcode == 8:
            p[c] = 1 if a == b else 0

def run_amplifiers(phases, pgm):
    inputs = [0]
    signals = inputs
    for phase in phases:
        signals = run_program(pgm, itertools.chain([phase], signals))

    # feedback
    for s in signals:
        inputs.append(s)
    return s

with open('../day_7.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

max_output = max(run_amplifiers(phases, pgm) for phases in itertools.permutations(range(5)))
print('part 1:', max_output)

max_output = max(run_amplifiers(phases, pgm) for phases in itertools.permutations(range(5, 10)))
print('part 2:', max_output)
