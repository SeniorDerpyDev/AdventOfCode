FLOOR, EMPTY, OCCUPIED = 0, 1, 2
tr = {'.': 0, 'L': EMPTY, '#': OCCUPIED}

with open('../day_11.txt', 'r') as f:
    initial_layout = [[tr[c] for c in "." + line.rstrip() + "."] for line in f]

X = len(initial_layout[0])
initial_layout.insert(0, [FLOOR] * X)
initial_layout.append([FLOOR] * X)
Y = len(initial_layout)

adj = [(i,j) for i in [-1, 0, 1] for j in [-1, 0, 1]]
def adjacent(l, x, y):
    return sum(l[y+i][x+j] == OCCUPIED for i, j in adj)

steps = [(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
def line_of_sight(l, x, y):
    count = 0
    for dy, dx in steps:
        cx, cy = x + dx, y + dy
        while 0 < cx < X-1 and 0 < cy < Y-1 and l[cy][cx] == FLOOR:
            cx += dx; cy += dy
        if l[cy][cx] == OCCUPIED:
            count += 1;
    return count

def do_the_work(layout, counter):
    changed = True
    while changed:
        next_layout = [row[:] for row in layout]
        changed = False
        for y in range(1, Y-1):
            for x in range(1, X-1):
                p = layout[y][x]
                if p == FLOOR:
                    continue
                c = counter(layout, x, y)
                if p == EMPTY and c == 0:
                    next_layout[y][x] = OCCUPIED
                    changed = True
                elif p == OCCUPIED and c > 4:
                    next_layout[y][x] = EMPTY
                    changed = True
        layout = next_layout
    return sum(seat == OCCUPIED for row in layout for seat in row)

print("part 1 ", do_the_work(initial_layout, adjacent))
print("part 2 ", do_the_work(initial_layout, line_of_sight))
