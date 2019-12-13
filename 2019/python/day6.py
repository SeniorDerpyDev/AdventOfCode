orbit_map = {}

with open('../day_6.txt', 'r') as f:
    for l in f:
        center, satellite = l.rstrip().split(')')
        orbit_map[satellite] = center

orbit_count = 0
for k in orbit_map.keys():
    satellite = k
    while satellite != 'COM':
        orbit_count += 1
        satellite = orbit_map[satellite]

def get_orbits_for_satellite(s):
    while s != 'COM':
        s = orbit_map[s]
        yield s

you = set(get_orbits_for_satellite('YOU'))
santa = set(get_orbits_for_satellite('SAN'))
transfers = len(you ^ santa)

print('part 1:', orbit_count)
print('part 2:', transfers)
