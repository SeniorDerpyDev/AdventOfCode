import math

CUT, DEAL_INC, DEAL_NEW = 0, 1, 2

def parse(l):
    if l.startswith('cut'):
        return (CUT, int(l[4:]))
    if l.startswith('deal with increment'):
        return (DEAL_INC, int(l[20:]))
    if l.startswith('deal into new stack'):
        return (DEAL_NEW, None)
 
def shuffle_position(pos, n_cards):
    for (s, n) in shuffle:
        if s == CUT:
            pos = (pos - n) % n_cards
        elif s == DEAL_NEW:
            pos = n_cards - 1 - pos
        elif s == DEAL_INC:
            pos = (pos * n) % n_cards
    return pos

def shuffle_position_rev(pos, n_cards):
    for (s, n) in reversed(shuffle):
        if s == CUT:
            pos = (pos + n) % n_cards
        elif s == DEAL_NEW:
            pos = n_cards - 1 - pos
        elif s == DEAL_INC:
            inv = pow(n, n_cards - 2, n_cards)
            pos = (pos * inv) % n_cards
    return pos

def compose_n_times(n, a, b, m):
    ra, rb = 1, 0
    while n != 0:
        if n & 1 == 1:
            ra, rb = (ra * a) % m, (ra * b + rb) % m
        n = n >> 1
        a, b = (a * a) % m, (a * b + b) % m
    return ra, rb

with open('../day_22.txt', 'r') as f:
    shuffle = [parse(l) for l in f]


cards = 10007
print('part 1:', shuffle_position(2019, cards))


cards      = 119315717514047
n_shuffles = 101741582076661

# shuffle(p) = (a * p + b) % cards 
b = shuffle_position_rev(0, cards)
a = shuffle_position_rev(1, cards) - b

an, bn = compose_n_times(n_shuffles, a, b, cards)

# suffle_n(p) = a^n * p + (a^(n-1) + a^(n-2) + ... + a^1 + 1) * b % cards
#             = a^n * p + (a^n - 1)/(a - 1) * b % cards 
# an = pow(a, n_shuffles, cards)
# bn = (an - 1) * pow(a - 1, cards - 2, cards) * b % cards

print('part 2:', (an * 2020 + bn) % cards)