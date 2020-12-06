with open('../day_6.txt', 'r') as f:
    answers = [[set(person) for person in group.split()] for group in f.read().split('\n\n')]

p1 = sum(len(set.union(*group)) for group in answers)
p2 = sum(len(set.intersection(*group)) for group in answers)

print('part 1:', p1)
print('part 2:', p2)

