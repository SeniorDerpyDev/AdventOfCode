from collections import defaultdict
FS = defaultdict(int)
ctx = []
for line in open(0):
    line = line.strip()
    if line[0:4] == '$ cd':
        if line[5:] == '/':
            ctx = []
        elif line[5:] == '..':
            ctx.pop()
        else:
            ctx.append(line[5:])
    elif line[0] != '$':
        s = line.split()[0]
        if s.isdecimal():
            for n in range(len(ctx)+1):
                FS[tuple(ctx[0:n])] += int(s)

print(sum(s for s in FS.values() if s <= 100_000))
print(min(s for s in FS.values() if s > FS[()] - 40_000_000))

