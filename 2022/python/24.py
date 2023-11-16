G = [list(l.strip()) for l in open(0)]
R, C = len(G), len(G[0])
BD = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}
B = [(r, c, G[r][c]) for r in range(R) for c in range(C) if G[r][c] in BD]

S = (0, next(i for i in range(C) if G[0][i] == '.'))
E = (R-1, next(i for i in range(C) if G[-1][i] == '.'))

batch = set([S])
t = 0
stage = 0
ans = [0, 0, 0]
goals = [E, S, E]
while stage < 3:
    NB = []
    for br, bc, d in B:
        br += BD[d][0]
        bc += BD[d][1]
        if br == 0:
            br = R-2
        if br == R-1:
            br = 1
        if bc == 0:
            bc = C-2
        if bc == C-1:
            bc = 1
        NB.append((br, bc, d))
    XX = set((r, c) for r, c, _ in NB)

    next_batch = set()
    for r, c in batch:
        if goals[stage] == (r, c):
            ans[stage] = t
            stage += 1
            next_batch = set([(r, c)])
            break
        for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if 0<=nr<R and 0<=nc<C and G[nr][nc] != '#' and (nr, nc) not in XX:
                next_batch.add((nr, nc))
    B = NB
    batch = next_batch
    t += 1

print(ans[0])
print(ans[2])


