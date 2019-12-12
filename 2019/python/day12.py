import re
from itertools import combinations
from math import gcd

X_AXIS, Y_AXIS, Z_AXIS = 0, 1, 2

# moon = [x, y, z, Vx, Vy, Vz]
def get_initial_state():
    with open('../day_12.txt') as f:
        return [[int(match) for match in re.findall(r'-?\d+', line)] + [0, 0, 0] for line in f]

def simulate(moons, axes):
    for (m0, m1) in combinations(moons, 2):
        for axis in axes:
            if m0[axis] < m1[axis]:
                m0[axis+3] += 1
                m1[axis+3] -= 1
            elif m0[axis] > m1[axis]:
                m0[axis+3] -= 1
                m1[axis+3] += 1
    for m in moons:
        for axis in axes:
            m[axis] += m[axis+3]

moons = get_initial_state()
for _ in range(1000):
    simulate(moons, [X_AXIS, Y_AXIS, Z_AXIS])
total_energy = sum( sum(abs(v) for v in m[0:3]) * sum(abs(v) for v in m[3:6]) for m in moons )
print('part 1:', total_energy)


def period(axis):
    steps = 0
    moons = get_initial_state()
    state0 = [m[axis::3] for m in moons]
    while True:
        steps += 1
        simulate(moons, [axis])
        state = [m[axis::3] for m in moons]
        if state == state0:
            break
    return steps

def lcm(a, b):
    return a * b // gcd(a, b)

print('part 2:', lcm(lcm(period(X_AXIS), period(Y_AXIS)), period(Z_AXIS)))
