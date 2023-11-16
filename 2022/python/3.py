lines = [l.strip() for l in open(0)]

p1 = 0
for l in lines:
    m = len(l) // 2
    item, = set(l[:m]) & set(l[m:])
    if 'a' <= item <= 'z':
        p1 += ord(item) - ord('a') + 1
    else:
        p1 += ord(item) - ord('A') + 27
print(p1)

p2 = 0
for i in range(0, len(lines), 3):
    item, = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
    if 'a' <= item <= 'z':
        p2 += ord(item) - ord('a') + 1
    else:
        p2 += ord(item) - ord('A') + 27
print(p2)
