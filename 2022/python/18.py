from collections import deque
cubes = set()
mx = my = mz = float("inf")
Mx = My = Mz = -float("inf")
for line in open(0):
    x, y, z = (int(s) for s in line.strip().split(','))
    cubes.add((x, y, z))
    mx = min(mx, x); Mx = max(Mx, x)
    my = min(my, y); My = max(My, y)
    mz = min(mz, z); Mz = max(Mz, z)
mx -= 1; my -= 1; mz -= 1
Mx += 1; My += 1; Mz += 1

ds = [(1,0,0), (0,1,0), (0,0,1), (-1,0,0), (0,-1,0), (0,0,-1)]

print(sum((x+dx, y+dy, z+dz) not in cubes for x, y, z in cubes for dx, dy, dz in ds))

air = set()
Q = deque()
Q.append((mx, my, mz))
while Q:
    x, y, z = c = Q.popleft()
    if c in air or c in cubes:
        continue
    air.add(c)
    for dx, dy, dz in ds:
        if mx <= x+dx <= Mx and my <= y+dy <= My and mz <= z+dz <= Mz:
            Q.append((x+dx, y+dy, z+dz))

print(sum((x+dx, y+dy, z+dz) in air for x, y, z in cubes for dx, dy, dz in ds))
