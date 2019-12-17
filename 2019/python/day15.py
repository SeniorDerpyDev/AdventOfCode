from collections import defaultdict

R, W = 0, 1
POS, IMMED, REL = 0, 1, 2

NORTH, SOUTH, WEST, EAST = 1, 2, 3, 4


parms = {
    1: (R, R, W), 2: (R, R, W), 3: (W,), 4: (R,),
    5: (R, R), 6: (R, R), 7: (R, R, W), 8: (R, R, W),
    9: (R,)
}

def run(pgm):
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

class Droid:
    moves = [NORTH, SOUTH, WEST, EAST]
    opposites = { NORTH: SOUTH, SOUTH: NORTH, WEST: EAST, EAST: WEST }

    def __init__(self, pgm):
        self.droid = run(pgm)
        self.current_path = []
        self.minutes = 0

    def move(self, m):
        next(self.droid)
        status = self.droid.send(m)
        if status != 0:
            self.current_path.append(m)
        return status

    def move_back(self):
        m = self.current_path.pop()
        next(self.droid)
        self.droid.send(Droid.opposites[m])

    def search(self, m):
        status = self.move(m)
        if status == 0:
            return False
        if status == 2:
            return True
        for n in Droid.moves:
            if n != Droid.opposites[m] and self.search(n):
                return True
        self.move_back()

    def fill(self, m):
        status = self.move(m)
        if status == 0:
            return
        self.minutes = max(self.minutes, len(self.current_path))
        for n in Droid.moves:
            if n != Droid.opposites[m]:
                self.fill(n)
        self.move_back()

    def find_oxygen_system(self):
        for m in Droid.moves:
            if self.search(m):
                break
        return len(self.current_path)

    def fill_oxygen(self):
        self.current_path = []
        for m in Droid.moves:
            self.fill(m)
        return self.minutes

with open('../day_15.txt', 'r') as f:
    pgm = [int(s) for s in f.read().rstrip().split(',')]

d = Droid(pgm)
print('Part 1:', d.find_oxygen_system())

print('Part 2:', d.fill_oxygen())
