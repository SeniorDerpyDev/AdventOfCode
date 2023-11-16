import re
from itertools import permutations

V = {}
F = {}
for line in open(0):
    line = line.strip()
    v = line.split()[1]
    V[v] = re.split("to valves? ", line)[1].split(', ')
    f = int(next(re.finditer("\d+", line))[0])
    if f > 0: F[v] = f

I = { v: 1 << i for i, v in enumerate(F) }
D = { (v1, v2): 1 if v2 in V[v1] else 1000 for v1 in V for v2 in V }
for k, i, j in permutations(V, 3):
    D[i, j] = min(D[i, j], D[i, k] + D[k, j])

def solve(time, v, used, r, p):
    r[used] = max(r.get(used, 0), p)
    for nv, f in F.items():
        t = time - D[v, nv] - 1
        if I[nv] & used or t <= 0:
            continue
        solve(t, nv, used | I[nv], r, p + f*t)

R = {}
solve(30, 'AA', 0, R, 0)
print(max(R.values()))

R = {}
solve(26, 'AA', 0, R, 0)
print(max(v1 + v2 for k1, v1 in R.items() for k2, v2 in R.items() if k1 & k2 == 0))
