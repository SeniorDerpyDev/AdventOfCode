with open('../day_12.txt', 'r') as f:
    nav = [(line[0], int(line[1:])) for line in f]

rotation = { 90: 1j, 180: -1, 270: -1j }
compass = {'N': 1j, 'S': -1j, 'E': 1, 'W': -1}

pos, heading = 0 + 0j, 1 + 0j
for c, n in nav:
    if c == 'F':
        pos += n * heading
    elif c == 'L':
        heading *= rotation[n]
    elif c == 'R':
        heading *= rotation[360-n]
    elif c in compass:
        pos += n * compass[c]
print("part 1 ", int(abs(pos.real) + abs(pos.imag)))

pos, waypoint = 0 + 0j, 10 + 1j
for c, n in nav:
    if c == 'F':
        pos += n * waypoint
    elif c == 'L':
        waypoint *= rotation[n]
    elif c == 'R':
        waypoint *= rotation[360-n]
    elif c in compass:
        waypoint += n * compass[c]
print("part 2 ", int(abs(pos.real) + abs(pos.imag)))
