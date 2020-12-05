from functools import reduce

with open('../day_5.txt', 'r') as f:
    trans = str.maketrans('FBLR', '0101')
    passes = [int(s.rstrip().translate(trans), 2) for s in f]

(min_id, max_id, total) = reduce(lambda acc, id : (min(acc[0], id), max(acc[1], id), acc[2] + id), passes, (1024, 0, 0))

print('part 1:', max_id)
print('part 1:', (max_id + min_id) * (max_id - min_id + 1) // 2 - total)
