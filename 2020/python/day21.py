ingredients_per_alergen = {}
foods = []
with open('../day_21.txt') as f:
    for line in f:
        i = line.find('(')
        ingredients = set(line[:i].split())
        foods.append(ingredients)
        for alergen in line[i+10:-2].split(', '):
            if alergen in ingredients_per_alergen:
                ingredients_per_alergen[alergen] &= ingredients
            else:
                ingredients_per_alergen[alergen] = ingredients.copy()

bad_ingredients = set.union(*ingredients_per_alergen.values())
print('part 1:', sum(len(food - bad_ingredients) for food in foods))

dangerous_list = []
found = set()
while len(dangerous_list) != len(ingredients_per_alergen):
    for a, i in ingredients_per_alergen.items():
        if len(i - found) == 1:
            dangerous_list.append((a, (i - found).pop()))
            found |= i
dangerous_list.sort()
print('part 2:', ','.join(i for _, i in dangerous_list))
