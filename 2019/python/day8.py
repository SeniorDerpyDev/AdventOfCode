from collections import Counter

with open('../day_8.txt') as f:
    data = f.readline().rstrip()

width, height = 25, 6
size = width * height
layers = [data[n:n+size] for n in range(0, len(data), size)]

counter = min((Counter(l) for l in layers), key = lambda c : c['0'])
print('part 1:', counter['1'] * counter['2']) 

img = bytearray(b' ' * size)
for layer in reversed(layers):
    for i, c in enumerate(layer):
        if c == '0':
            img[i] = ord(' ')
        elif c == '1':
            img[i] = ord('#')

print('part 2:')
for i in range(0, size, width):
    print(img[i:i+width].decode()) 
