from itertools import product

with open('../day_19.txt') as f:
    rules = {}
    for line in f:
        if line == '\n':
            break
        left, right = line.split(': ')
        if right[0] == '"':
            rules[left] = right[1]
        else:
            rules[left] = [list(s.split()) for s in right.split(' | ')]
    messages = [line.rstrip() for line in f]

def build_valid_messages(rule):
    r = rules[rule]
    if type(r) == str:
        return set(r)

    s = set()
    for or_rule in r:
        l = [build_valid_messages(subrule) for subrule in or_rule]
        s.update(''.join(t) for t in product(*l))
    return s

valid_0 = build_valid_messages('0')
print('part 1:', sum(m in valid_0 for m in messages))

valid_42 = build_valid_messages('42')
valid_31 = build_valid_messages('31')

# messages for rules 42 and 31 have length 8
def valid_part_2(msg):
    n42, n31 = 0, 0
    for i in range(0, len(msg), 8):
        if msg[i:i+8] in valid_42 and n31 == 0:
            n42 += 1
        elif msg[i:i+8] in valid_31:
            n31 += 1
        else:
            return False
    return n42 > n31 > 0

print('part 2:', sum(valid_part_2(m) for m in messages))

