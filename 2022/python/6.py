line = open(0).read().strip()

for n in range(4, len(line)):
    if len(set(line[n-4:n])) == 4:
        print(n)
        break

for n in range(14, len(line)):
    if len(set(line[n-14:n])) == 14:
        print(n)
        break
