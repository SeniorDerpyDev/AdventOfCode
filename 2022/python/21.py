from operator import add, sub, mul, truediv

M = { s[0][:-1] : int(s[1]) if s[1].isdecimal() else s[1:] for s in (l.strip().split() for l in open(0)) }
O = { '+': add, '-': sub, '*': mul, '/': truediv }

def solve(m, h=None):
    if m == 'humn' and h:
        return h
    if type(M[m]) == int:
        return M[m]
    m1, op, m2 = M[m]
    return O[op](solve(m1, h), solve(m2, h))

print(int(solve('root')))

M['root'][1] = '-'
a, b = 0, pow(10, 14)
ra = solve('root', a)
rb = solve('root', b)
if ra > rb:
    a, ra, b, rb = b, rb, a, ra
while True:
    m = (a + b) // 2
    rm = solve('root', m)
    if rm > 0:
        b, rb = m, rm
    elif rm < 0:
        a, ra = m, rm
    else:
        print(m)
        break
