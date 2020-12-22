import re
from functools import reduce
from operator import mul

def calc1(s):
    tokens = re.split(' ([*+]) ', s)
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        if tokens[i] == '+':
            result += int(tokens[i+1])
        else:
            result *= int(tokens[i+1])
    return result

def calc2(s):
    return reduce(mul, ((sum(int(n) for n in expr.split(' + '))) for expr in s.split(' * ')))

def evaluate(s, f):
    m = re.search('\([\d\s*+]+\)', s)
    while m:
        b, e = m.span()
        s = s[:b] + str(evaluate(s[b+1:e-1], f)) + s[e:]
        m = re.search('\([\d\s*+]+\)', s)
    return f(s)

lines = open('../day_18.txt', 'r').read().splitlines()
print('part 1:', sum(evaluate(l, calc1) for l in lines))
print('part 2:', sum(evaluate(l, calc2) for l in lines))
