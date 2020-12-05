with open('../day_5.txt', 'r') as f:
    trans = str.maketrans('FBLR', '0101')
    passes = [int(s.rstrip().translate(trans), 2) for s in f]
    passes.sort()

p1 = passes[-1]

lo, hi = 0, len(passes)
while lo != hi:
    m = lo + (hi - lo) // 2
    if passes[m] == passes[0] + m:
        lo = m + 1
    else:
        hi = m
p2 = passes[0] + lo

print('part 1:', p1)
print('part 1:', p2)
