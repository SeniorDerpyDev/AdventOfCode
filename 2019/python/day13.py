from collections import defaultdict

R, W = 0, 1
POS, IMMED, REL = 0, 1, 2

EMPTY, WALL, BLOCK, PADDLE, BALL = range(5)

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

def cmp(a, b):
    return (a > b) - (a < b)

def play_game(pgm, *, coins=None):
    score, ball_x, paddle_x = 0, -1, -1
    screen = {}
    if coins:
        pgm[0] = coins
    outputs = run(pgm, lambda : cmp(ball_x, paddle_x))
    while True:
        try:
            x = next(outputs)
            y = next(outputs)
            if (x, y) == (-1, 0):
                score = next(outputs)
            else:
                tile = next(outputs)
                screen[(x, y)] = tile
                if tile == BALL:
                    ball_x = x
                elif tile == PADDLE:
                    paddle_x = x

        except StopIteration:
            break

    return screen, score


with open('../day_13.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

screen, _ = play_game(pgm)
print('part 1:', sum(1 for v in screen.values() if v == BLOCK))

_, score = play_game(pgm, coins=2)
print('part 2:', score)
