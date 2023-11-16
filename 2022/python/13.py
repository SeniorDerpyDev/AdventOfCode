def cmp(l, r):
    if type(l) == int:
        if type(r) == int:
            return l - r
        else:
            return cmp([l], r)
    if type(r) == int:
        return cmp(l, [r])

    for li, ri in zip(l, r):
        c = cmp(li, ri)
        if c != 0:
            return c

    return len(l) - len(r)

inp = open(0).read().strip()
ans = 0
for i, p in enumerate(inp.split('\n\n')):
    l, r = (eval(s) for s in p.split())
    if cmp(l, r) < 0:
        ans += i+1
print(ans)

lt2 = 0
lt6 = 1
for line in inp.splitlines():
    if not line:
        continue
    p = eval(line)
    if cmp(p, [[2]]) < 0:
        lt2 += 1
    if cmp(p, [[6]]) < 0:
        lt6 += 1
print((lt2+1) * (lt6+1))
