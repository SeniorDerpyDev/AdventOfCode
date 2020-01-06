from collections import defaultdict

R, W = 0, 1

POS, IMMED, REL = 0, 1, 2

parms = {
    1: (R, R, W), 2: (R, R, W), 3: (W,), 4: (R,),
    5: (R, R), 6: (R, R), 7: (R, R, W), 8: (R, R, W),
    9: (R,)
}

def run(pgm, inp=None):
    output = None
    ip = 0
    base_address = 0
    p = defaultdict(int, enumerate(pgm))

    while p[ip] != 99:
        modes, opcode = divmod(p[ip], 100)
        ip += 1

        args = [0, 0, 0]
        for n, rw in enumerate(parms[opcode]):
            val, ip = p[ip], ip + 1
            modes, m = divmod(modes, 10)
            if rw == R:
                if m == POS:
                    val = p[val]
                elif m == REL:
                    val = p[base_address + val]
            elif rw == W and m == REL:
                val = base_address + val
            args[n] = val

        a, b, c = args
        if opcode == 1:
            p[c] = a + b
        elif opcode == 2:
            p[c] = a * b
        elif opcode == 3:
            p[a] = next(inp)
        elif opcode == 4:
            yield a
            output = a
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
        elif opcode == 9:
            base_address += a

    return output


with open('../day_21.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

script = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
AND D J
WALK
"""

hull_damage = next(i for i in run(pgm, (ord(c) for c in script)) if i > 127)
print('part 1:', hull_damage)


script = """NOT A T
NOT B J
OR T J
NOT C T
OR T J
NOT E T
AND H T
OR E T
AND T J
AND D J
RUN
"""

hull_damage = next(i for i in run(pgm, (ord(c) for c in script)) if i > 127)
print('part 2:', hull_damage)