with open('../day_16.txt', 'r') as f:
    input_signal = f.read().strip()
    signal = [int(c) for c in input_signal]

lst = signal[:]
length = len(lst)
pattern = [0, 1, 0, -1]
for _ in range(100):
    for i in range(length):
        lst[i] = abs(sum(pattern[(j + 1) // (i + 1) % 4] * lst[j] for j in range(i, length))) % 10
print('part 1:', ''.join(str(i) for i in lst[:8]))


offset = int(input_signal[0:7])
lst = (signal * 10_000)[offset:]
length = len(lst)
for _ in range(100):
    for i in range(length - 1, 0, -1):
        lst[i-1] = (lst[i-1] + lst[i]) % 10
print('part 2:', ''.join(str(i) for i in lst[:8]))
