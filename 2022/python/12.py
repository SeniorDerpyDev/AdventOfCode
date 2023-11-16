G = [list(line.strip()) for line in open(0)]
R, C = len(G), len(G[0])

for r in range(R):
    for c in range(C):
        if G[r][c] == 'S':
            G[r][c] = 'a'
            sr, sc = r, c
        if G[r][c] == 'E':
            G[r][c] = 'z'
            er, ec = r, c

batch = [(sr, sc)]
V = set()
d = 0
ans = 0
while ans == 0:
    new_batch = []
    for r, c in batch:
        if (r, c) in V:
            continue
        V.add((r,c))
        if (r, c) == (er, ec):
            ans = d
            break
        for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if 0<=nr<R and 0<=nc<C and (ord(G[nr][nc]) - ord(G[r][c])) <= 1:
                new_batch.append((nr, nc))
    batch = new_batch
    d += 1
print(ans)

batch = [(er, ec)]
V = set()
d = 0
ans = 0
while ans == 0:
    new_batch = []
    for r, c in batch:
        if (r, c) in V:
            continue
        V.add((r,c))
        if G[r][c] == 'a':
            ans = d
            break
        for nr, nc in (r+1, c), (r-1, c), (r, c+1), (r, c-1):
            if 0<=nr<R and 0<=nc<C and (ord(G[nr][nc]) - ord(G[r][c])) >= -1:
                new_batch.append((nr, nc))
    batch = new_batch
    d += 1
print(ans)
