import heapq

neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]
OUTER, INNER = 0, 1

def build_graph(m, start):
    portals = dict()
    w, h = len(m[0]), len(m)
    for y in range(2, h - 2):
        for x in range(2, w - 2):
            if m[y][x] != '.':
                continue

            if m[y][x-2:x].isalpha():
                name = m[y][x-2:x]
            elif m[y][x+1:x+3].isalpha():
                name = m[y][x+1:x+3]
            elif (m[y-2][x]+m[y-1][x]).isalpha():
                name = m[y-2][x]+m[y-1][x]
            elif (m[y+1][x]+m[y+2][x]).isalpha():
                name = m[y+1][x]+m[y+2][x]
            else:
                continue

            if name == start:
                start_pos = (x, y)
            elif x == 2 or y == 2 or x == w - 3 or y == h - 3:
                portals[x,y] = (name, OUTER)
            else:
                portals[x,y] = (name, INNER)

    g = {portal : find_adjacent(maze, portals, pos) for pos, portal in portals.items()}
    g[start] = find_adjacent(maze, portals, start_pos)
    return g

def find_adjacent(maze, portals, pos):
    visited = {pos}
    adjacent = []
    x, y = pos
    cells = [(x+dx, y+dy, 1) for (dx, dy) in neighbours if maze[y+dy][x+dx] == '.']

    while cells:
        (x, y, steps) = cells.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if (x, y) in portals:
            adjacent.append((portals[x, y], steps))
        else:
            cells.extend([(x+dx, y+dy, steps + 1) for (dx, dy) in neighbours if maze[y+dy][x+dx] == '.'])
    return adjacent

def walk_maze(g, start, goal):
    visited = {start}
    q = [(dist, portal) for portal, dist in g[start]]
    heapq.heapify(q)

    while q:
        (dist, portal) = heapq.heappop(q)
        if portal[0] == goal:
            return dist
        if portal in visited:
            continue

        name, type = portal
        for next, d in g[(name, 1-type)]:
            heapq.heappush(q, (dist + d + 1, next))
        visited.add(portal)

def walk_maze_levels(g, start, goal):
    visited = {(start, 0)}
    q = [(dist, 0, portal) for portal, dist in g[start]]
    heapq.heapify(q)

    while q:
        (dist, lvl, portal) = heapq.heappop(q)
        if portal[0] == goal:
            if lvl == 0:
                return dist
            else:
                continue
        if (portal, lvl) in visited:
            continue

        name, type = portal
        for next, d in g[(name, 1-type)]:
            if type == INNER:
                heapq.heappush(q, (dist + d + 1, lvl + 1, next))
            elif lvl > 0:
                heapq.heappush(q, (dist + d + 1, lvl - 1, next))
        visited.add((portal, lvl))


with open('../day_20.txt', 'r') as f:
    maze = f.read().splitlines()

g = build_graph(maze, 'AA')
print('part 1:', walk_maze(g, 'AA', 'ZZ'))
print('part 2:', walk_maze_levels(g, 'AA', 'ZZ'))
