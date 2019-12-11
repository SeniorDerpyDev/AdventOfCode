from collections import defaultdict

R, W = 0, 1
POS, IMMED, REL = 0, 1, 2

BLACK, WHITE = 0, 1
LEFT, RIGHT = 0, 1

parms = {
    1: (R, R, W), 2: (R, R, W), 3: (W,), 4: (R,),
    5: (R, R), 6: (R, R), 7: (R, R, W), 8: (R, R, W),
    9: (R,)
}

def run(pgm, inp):
    output = None
    ip = 0
    base_address = 0
    p = defaultdict(int)
    for i, v in enumerate(pgm):
        p[i] = v

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
            p[a] = inp()
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
        elif opcode == 9:
            base_address += a
    return output

def robot(panels, pgm):
    curr_x, curr_y = 0, 0
    dx, dy = 0, -1
    outputs = run(pgm, lambda : panels[(curr_x, curr_y)])
    while True:
        try:
            panels[(curr_x, curr_y)] = next(outputs)
            if next(outputs) == RIGHT:
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
            curr_x += dx
            curr_y += dy
        except StopIteration:
            break

with open('../day_11.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

panels = defaultdict(int)
robot(panels, pgm)
print('part 1:', len(panels))

panels = defaultdict(int)
panels[(0, 0)] = WHITE
robot(panels, pgm)
print('part 2:')
output = bytearray(b' ' * (8*5) )
for y in range(6):
    for x in range(40):
        output[x] = ord('#') if panels[(x, y)] == WHITE else ord(' ')
    print(output.decode())
