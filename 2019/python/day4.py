def has_two_consecutive(s):
    return any(l == r for (l, r) in zip(s[:-1], s[1:]))

def never_decrease(s):
    return all(l <= r for (l, r) in zip(s[:-1], s[1:]))

def groups(s):
    l = len(s)
    i, j = 0, 0
    while i < l:
        while j < l and s[i] == s[j]:
            j += 1
        yield s[i:j]
        i = j

def has_a_group_of_two(s):
    return any(len(g) == 2 for g in groups(s))

with open('../day_4.txt', 'r') as f:
     first, last = map(int, f.readline().rstrip().split('-'))

pwd_range = (str(n) for n in range(first, last + 1))

candidates1 = [p for p in pwd_range if has_two_consecutive(p) and never_decrease(p)]
print('part 1:', len(candidates1))

candidates2 = [p for p in candidates1 if has_a_group_of_two(p)]
print('part 2:', len(candidates2))
