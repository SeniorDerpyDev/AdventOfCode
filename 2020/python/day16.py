from itertools import chain
from functools import reduce
from operator import mul

with open('../day_16.txt', 'r') as f:
    rules, my_ticket, nearby_tickets = f.read().split('\n\n')

fields = {}
for line in rules.splitlines():
    l, r = line.split(': ')
    fields[l] = [tuple(int(n) for n in s.split('-')) for s in r.split(' or ')]

my_ticket = [int(n) for n in my_ticket.splitlines()[1].split(',')]
nearby_tickets = [[int(n) for n in line.split(',')] for line in nearby_tickets.splitlines()[1:]]
all_rules = list(chain.from_iterable(fields.values()))

total = 0
valid_tickets = []
for ticket in nearby_tickets:
    not_ok = [n for n in ticket if all(n < t0 or n > t1 for t0, t1 in all_rules)]
    if not_ok:
        total += sum(not_ok)
    else:
        valid_tickets.append(ticket)
print('part 1:', total)

fields_positions = {}
while len(fields_positions) != 20:
    for i in range(20):
        maybe = [f for f, rules in fields.items() if all(any(t0 <= ticket[i] <= t1 for t0, t1 in rules) for ticket in valid_tickets)]
        if len(maybe) == 1:
            fields_positions[maybe[0]] = i
            del fields[maybe[0]]

p2 = reduce(mul, (my_ticket[i] for f, i in fields_positions.items() if f.startswith('departure')))
print('part 2:', p2)

