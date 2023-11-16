stacks, moves = open(0).read().split('\n\n')

L = []
for line in stacks.splitlines()[:-1]:
    L.append([line[i] for i in range(1, len(line), 4)])

M = []
for m in moves.splitlines():
    _, n, _, f, _, t = m.split()
    M.append((int(n), int(f)-1, int(t)-1))

S = [list(t) for t in zip(*L[::-1])]
S = [[c for c in s if c != ' '] for s in S]
for n, f, t in M:
    S[t] += S[f][-n:][::-1]
    del S[f][-n:]
print(''.join(s[-1] for s in S))

S = [list(t) for t in zip(*L[::-1])]
S = [[c for c in s if c != ' '] for s in S]
for n, f, t in M:
    S[t] += S[f][-n:]
    del S[f][-n:]
print(''.join(s[-1] for s in S))

