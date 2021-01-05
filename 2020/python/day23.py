def make_moves(start, n, hi):
    curr = start
    for _ in range(n):
        dest = curr
        while True:
            dest = dest - 1
            if dest == 0:
                dest = hi
            if dest != cups[curr] and dest != cups[cups[curr]] and dest != cups[cups[cups[curr]]]:
                break
        third = cups[cups[cups[curr]]]
        cups[dest], cups[curr], cups[third] = cups[curr], cups[third], cups[dest]
        curr = cups[curr]

INPUT = '156794823'

cups = [0] * 10
for i in range(len(INPUT)-1):
    cups[int(INPUT[i])] = int(INPUT[i+1])
cups[int(INPUT[-1])] = int(INPUT[0])

make_moves(int(INPUT[0]), 100, 9)

p1 = ''
n = 1
while cups[n] != 1:
    p1 += str(cups[n])
    n = cups[n]
print('part 1:', p1)


cups = [0] * 1000001
for i in range(len(INPUT)-1):
    cups[int(INPUT[i])] = int(INPUT[i+1])
cups[int(INPUT[-1])] = 10
for n in range(10, 1000000):
    cups[n] = n+1
cups[1000000] = int(INPUT[0])

make_moves(int(INPUT[0]), 10000000, 1000000)

p2 = cups[1]* cups[cups[1]]
print('part 2:', p2)
