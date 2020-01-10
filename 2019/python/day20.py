from collections import defaultdict

adjacent = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def find_portals(m):
    entries = defaultdict(list)
    w, h = len(m[0]), len(m)

    # horizontal portals
    for y in range(2, h - 2):
        x = 0
        while x < w - 1:
            name = m[y][x] + m[y][x + 1]
            if name.isalpha():
                if m[y][x - 1] == '.':
                    entries[name].append((x - 1, y))
                    x += 1
                else:
                    entries[name].append((x + 2, y))
                    x += 2
            x += 1

    # vertical portals
    for x in range(2, w - 2):
        y = 0
        while y < h - 1:
            name = m[y][x] + m[y + 1][x]
            if name.isalpha():
                if m[y - 1][x] == '.':
                    entries[name].append((x, y - 1))
                    y += 1
                else:
                    entries[name].append((x, y + 2))
                    y += 2
            y += 1

    start = entries.pop('AA')[0]
    end = entries.pop('ZZ')[0]
    portals = {}
    for name, entries in entries.items():
        portals[entries[0]] = entries[1]
        portals[entries[1]] = entries[0]

    return portals, start, end

def copy_maze(m):
    return [list(l) for l in maze]

def walk_maze(maze, portals, start, end):
    maze = copy_maze(maze)
    portals = dict(portals)
    cells = [(*start, 0, False)]
    while cells:
        (x, y, s, warped) = cells.pop(0)

        if (x, y) == end:
            return s

        if maze[y][x] != '.':
            continue

        if not warped and (x, y) in portals:
            exit = portals[x, y]
            cells.append((*exit, s + 1, True))
        else:
            cells.extend([(x + dx, y + dy, s + 1, False) for (dx, dy) in adjacent])

        maze[y][x] = '+'

def walk_maze_levels(maze, portals, start, end):
    w, h = len(maze[0]), len(maze)
    levels = {}
    cells = [(*start, 0, False)]
    while cells:
        (x, y, l, s, warped) = cells.pop(0)

        if (x, y, l) == end:
            return s

        m = levels.setdefault(l, copy_maze(maze))
        if m[y][x] != '.':
            continue

        if not warped and (x, y) in portals:
            exit = portals[x, y]
            # outer portal
            if x == 2 or y == 2 or x == w - 3 or y == h - 3:
                if l > 0:
                    cells.append((*exit, l - 1, s + 1, True))
            else:
                cells.append((*exit, l + 1, s + 1, True))
        else:
            cells.extend([(x + dx, y + dy, l, s + 1, False) for (dx, dy) in adjacent])

        m[y][x] = '+'

with open('../day_20.txt', 'r') as f:
    maze = [list(line) for line in f.read().splitlines()]

portals, start, end = find_portals(maze)

print('part 1:', walk_maze(maze, portals, start, end))
print('part 2:', walk_maze_levels(maze, portals, (*start, 0), (*end, 0)))
