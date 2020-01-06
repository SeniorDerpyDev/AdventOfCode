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

def print_scaffolding(s):
    print('  ', (' '*9).join(str(i) for i in range(5)))
    print('  ', ''.join(str(i%10) for i in range(41)))
    for i, l in enumerate(s):
        print(f'{i:02} {l}')

neighbours = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def find_intersections(s):
    height, width = len(s), len(s[0])
    def is_intersection(x, y):
        return s[y][x] == '#' and all(s[y+a][x+b] == '#' for (a,b) in neighbours)

    return [(x, y) for y in range(1, height - 1) for x in range(1, width - 1) if is_intersection(x, y)]

with open('../day_17.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

scaffolding = [l for l in ''.join(chr(c) for c in run(pgm)).splitlines() if len(l) > 0]
print('part 1:', sum(x * y for (x, y) in find_intersections(scaffolding)))



robot_dirs = { '^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

def get_moves(scaffolding):
    s = scaffolding
    height, width = len(s), len(s[0])
    x, y = next((x, y) for y in range(height) for x in range(width) if s[y][x] in robot_dirs.keys())
    dx, dy = robot_dirs[s[y][x]]

    def is_scaffold(x, y):
        return 0 <= x < width and 0 <= y < height and s[y][x] == '#'

    def turn_left():
        return dy, -dx

    def turn_right():
        return -dy, dx

    def get_next_move():
        nonlocal x, y, dx, dy
        count = 0
        while is_scaffold(x + dx, y + dy):
            count += 1
            x += dx
            y += dy
        if count:
            return str(count)

        rx, ry = turn_right()
        if is_scaffold(x + rx, y + ry):
            dx, dy = rx, ry
            return 'R'

        lx, ly = turn_left()
        if is_scaffold(x + lx, y + ly):
            dx, dy = lx, ly
            return 'L'

    moves = []
    move = get_next_move()
    while move:
        moves.append(move)
        move = get_next_move()
    return moves

def reduce(lst, sub):
    candidates = []
    size = 11   # each line has max size of 20 chars including ',' (11 chars + 9 ',')
    i = 0
    while lst[i] in 'ABC':
        i += 1
    while any(c in lst[i : i+size] for c in 'ABC'):
        size -= 1

    while size > 1:
        candidate = lst[:]
        j = i
        segment = lst[i : i+size]
        while j + size <= len(candidate):
            if segment == candidate[j : j+size]:
                candidate[j : j+size] = [sub]
            j += 1
        candidates.append((segment, candidate))
        size -= 1

    return candidates

def reduce_all(moves):
    for (segA, lstA) in reduce(moves, 'A'):
        for (segB, lstB) in reduce(lstA, 'B'):
            for (segC, lstC) in reduce(lstB, 'C'):
                if all(v in 'ABC' for v in lstC):
                    return [lstC, segA, segB, segC]

moves = get_moves(scaffolding)
instructions = '\n'.join(','.join(l) for l in reduce_all(moves)) + '\nn\n'

pgm[0] = 2
dust_amount = next(i for i in run(pgm, (ord(c) for c in instructions)) if i > 127)
print('part 2:', dust_amount)
