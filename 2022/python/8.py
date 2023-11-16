G = [list(line.strip()) for line in open(0)]
R = len(G)
C = len(G[0])

ans = 0
for r in range(R):
    for c in range(C):
        if all(G[x][c] < G[r][c] for x in range(0, r)):
            ans += 1
        elif all(G[x][c] < G[r][c] for x in range(r+1, R)):
            ans += 1
        elif all(G[r][x] < G[r][c] for x in range(0, c)):
            ans += 1
        elif all(G[r][x] < G[r][c] for x in range(c+1, C)):
            ans += 1
print(ans)

best = 0
for r in range(1, R-1):
    for c in range(1, C-1):
        score = 1
        for dr, dc in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            s = 0
            rr = r+dr; cc = c+dc
            while 0<=rr<R and 0<=cc<C:
                s += 1
                if G[rr][cc] >= G[r][c]:
                    break
                rr += dr; cc += dc
            score *= s
        best = max(best, score)
print(best)


