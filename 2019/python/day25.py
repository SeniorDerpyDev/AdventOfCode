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
            p[a] = yield
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


with open('../day_25.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

droid = run(pgm)
i = next(droid)
while True:
    while i:
        print(chr(i), end='')
        i = next(droid)
    cmd = input()
    for c in cmd:
        droid.send(ord(c))
    i = droid.send(10)


"""
items:
  hologram
  space law space brochure
  mutex
  manifold
"""
