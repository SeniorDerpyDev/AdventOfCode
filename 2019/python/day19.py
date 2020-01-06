from collections import defaultdict
from fractions import Fraction

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


with open('../day_19.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

print('part 1:', sum(run(pgm, iter((x, y))) for y in range(50) for x in range(50)))

def is_inside_tractor_beam(x, y):
    return run(pgm, iter((x, y)))

x, y = 100, 1
while not is_inside_tractor_beam(x, y+1):
    y += 1
slope1 = Fraction(y, x)

x, y = 1, 100
while not is_inside_tractor_beam(x+1, y):
    x += 1
slope2 = Fraction(y, x)

aprox_x = 99*(1+slope1)/(slope2-slope1)
aprox_y = 99*(1+1/slope2)/(1/slope1-1/slope2)

x, y = int(aprox_x), int(aprox_y)
while True:
    last_x, last_y = x, y
    while not is_inside_tractor_beam(x + 99, y):
        y += 1
    while not is_inside_tractor_beam(x, y + 99):
        x += 1
    if (last_x, last_y) == (x, y):
        break

print('part 2:', x*10000 + y)

