import re

required_fields = {
        'byr': lambda v : v.isdecimal() and 1920 <= int(v) <= 2002,
        'iyr': lambda v : v.isdecimal() and 2010 <= int(v) <= 2020,
        'eyr': lambda v : v.isdecimal() and 2020 <= int(v) <= 2030,
        'hgt': lambda v : (v.endswith('cm') and v[:-2].isdecimal() and 150 <= int(v[:-2]) <= 193) or
        (v.endswith('in') and v[:-2].isdecimal() and 59 <= int(v[:-2]) <= 76),
        'hcl': lambda v : re.match(r'\#[0-9a-f]{6}', v),
        'ecl': lambda v : v in {'amb','blu','brn','gry','grn','hzl','oth'},
        'pid': lambda v : v.isdecimal and len(v) == 9
        }

def parse(text):
    passports = ( dict( tuple(field_and_value.split(':')) for field_and_value in chunk.split() ) for chunk in text.split('\n\n') )
    return [p for p in passports if required_fields.keys() <= p.keys()]


with open('../day_4.txt', 'r') as f:
    passports = parse(f.read())

p1 = len(passports)
p2 = sum(1 for p in passports if all(validator(p[field]) for field, validator in required_fields.items()))

print('part 1:', p1)
print('part 2:', p2)

