from math import prod
M = []
for s in open(0).read().strip().split('\n\n'):
    ll = s.splitlines()
    items = [int(n) for n in ll[1].split(':')[1].split(',')]
    op = eval("lambda old:" + ll[2].split('=')[1])
    test = int(ll[3].split()[-1])
    t_true = int(ll[4].split()[-1])
    t_false = int(ll[5].split()[-1])
    M.append((items, op, test, t_true, t_false))

C = [0] * len(M)
mod = prod(m[2] for m in M)
for _ in range(10_000):
    for i, m in enumerate(M):
        for item in m[0]:
            item = m[1](item) % mod
            if item % m[2] == 0:
                M[m[3]][0].append(item)
            else:
                M[m[4]][0].append(item)
        C[i] += len(m[0])
        m[0].clear()
C.sort()
print(C[-2] * C[-1])

