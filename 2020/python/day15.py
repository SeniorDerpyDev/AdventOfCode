def memory_game(start_nums, target):
    numbers = {n: i for i, n in enumerate(start_nums)}
    n = 0
    for turn in range(len(start_nums), target - 1):
        numbers[n], n = turn, turn - numbers.get(n, turn)
    return n

INPUT = [7, 14, 0, 17, 11, 1, 2]

print('part 1:', memory_game(INPUT, 2020))
print('part 2:', memory_game(INPUT, 30000000))
