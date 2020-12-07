with open('../day_7.txt', 'r') as f:
    step1 = (line.rstrip(".\n").split(" bags contain") for line in f)
    step2 = ((t1, [x.split() for x in t2.split(",")]) for t1, t2 in step1)
    rules = {t1: [(int(l[0]), " ".join(l[1:3])) for l in t2 if l[0].isdecimal()] for t1, t2 in step2}

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
