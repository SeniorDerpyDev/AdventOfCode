def part1(signal):
    lst = signal[:]
    length = len(lst)
    for _ in range(100):
        prev = lst[:]
        for i in range(length//2+1):
            d, total = i + 1, 0
            n = i
            while n < length:
                total += sum(prev[n : n+d])
                n += d*4
            n = i + d*2
            while n < length:
                total -= sum(prev[n : n+d])
                n += d*4
            lst[i] = abs(total) % 10
        cumsum = 0
        for i in range(length - 1, length//2, -1):
            cumsum += lst[i]
            lst[i] = cumsum % 10

    return ''.join(str(i) for i in lst[:8])

def part2(signal, offset):
    lst = (signal * 10_000)[offset:]
    length = len(lst)
    for _ in range(100):
        cumsum = 0
        for i in range(length - 1, -1, -1):
            cumsum += lst[i]
            lst[i] = cumsum % 10
    return ''.join(str(i) for i in lst[:8])


with open('../day_16.txt', 'r') as f:
    input_signal = f.read().strip()
    signal = [int(c) for c in input_signal]

print('part 1:', part1(signal))
print('part 2:', part2(signal, int(input_signal[0:7])))
