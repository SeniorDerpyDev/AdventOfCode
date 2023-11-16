X = []
x = 1
for l in open(0):
    if l == "noop\n":
        X.append(x)
    else:
        X.append(x)
        X.append(x)
        x += int(l.split()[1])
print(sum(n*X[n-1] for n in range(20, len(X), 40)))

for r in range(0, len(X), 40):
    for c in range(40):
        print('#' if abs(X[r+c] - c) <= 1 else ' ', end='')
    print()
