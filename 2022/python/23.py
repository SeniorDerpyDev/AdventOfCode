from collections import defaultdict

E = {x + y*1j for y, l in enumerate(open(0)) for x, c in enumerate(l.strip()) if c == '#'}
D = [(-1j, -1j - 1, -1j + 1), (1j, 1j - 1, 1j + 1), (-1, -1 - 1j, -1 + 1j), (1, 1 - 1j, 1 + 1j)]
N = set(d for dd in D for d in dd)
i, moved = 0, True
while moved:
    MV = defaultdict(list)
    for e in E:
        if all(e + n not in E for n in N):
            MV[e].append(e)
            continue
        for dd in D:
            if all(e + d not in E for d in dd):
                MV[e + dd[0]].append(e)
                break
        else:
            MV[e].append(e)
    D = D[1:] + D[:1]

    E = set()
    moved = False
    for m in MV:
        if len(MV[m]) == 1:
            E.add(m)
            if m != MV[m][0]:
                moved = True
        else:
            E.update(MV[m])

    i += 1
    if i == 10:
        w = max(e.real for e in E) - min(e.real for e in E) + 1
        h = max(e.imag for e in E) - min(e.imag for e in E) + 1
        print(int(w * h) - len(E))
print(i)
