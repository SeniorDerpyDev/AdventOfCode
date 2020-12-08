import re

with open('../day_7.txt', 'r') as f:
    rules = { s1: [(int(n), b) for n,b in re.findall("(\d+) ([a-z ]+) bags?", s2)] for s1, s2 in
            (line.rstrip(".\n").split(" bags contain") for line in f) }

def part1(bag):
    s = set() 
    def impl(bag):
        for k, v in rules.items():
            if any(b == bag for _, b in v):
                s.add(k)
                impl(k)

    impl(bag)
    return len(s)

def part2(bag):
    return sum(n + n * part2(b) for n, b in rules[bag]) if bag in rules else 0

print("part 1:", part1("shiny gold"))
print("part 2:", part2("shiny gold"))
