E = [0]
for l in open(0):
    if l == '\n':
        E.append(0)
    else:
        E[-1] += int(l.strip())
E.sort()
print(E[-1])
print(sum(E[-3:]))

