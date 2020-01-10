from heapq import heappop, heappush

neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def build_graph(maze):
    graph = dict()
    starts = []
    i = 0
    w, h = len(maze[0]), len(maze)
    for y in range(h):
        for x in range(w):
            c = maze[y][x]
            if 'a' <= c <= 'z' or c == '@':
                if c == '@':
                    c += str(i)
                    i += 1
                    starts.append(c)
                graph[c] = find_adjacent(maze, (x, y))
    return graph, starts

def find_adjacent(maze, start):
    cells = [(*start, 0, set())]
    visited = set()
    adjacent = []

    while cells:
        (x, y, steps, doors) = cells.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        c = maze[y][x]
        if 'a' <= c <= 'z' and steps != 0:
            adjacent.append((c, steps, doors))
            continue
        if 'A' <= c <= 'Z':
            doors = doors | { c.lower() }

        cells.extend([(x+dx, y+dy, steps + 1, doors) for (dx, dy) in neighbours if maze[y+dy][x+dx] != '#'])
    return adjacent

def get_all_keys(g, starts, keys_to_collect):
    q = []
    heappush(q, (0, tuple(starts), frozenset()))
    visited = set()
    l = len(starts)

    while q:
        (steps, nodes, keys) = heappop(q)
        if (nodes, keys) in visited:
            continue
        if keys == keys_to_collect:
            return steps
        for i in range(l):
            lst = list(nodes)
            for (next, dist, doors) in g[nodes[i]]:
                if doors.issubset(keys):
                    lst[i] = next
                    heappush(q, (steps + dist, tuple(lst), keys | { next }))

        visited.add((nodes, keys))

with open('../day_18.txt', 'r') as f:
    maze = [list(line) for line in f.read().splitlines()]

graph, starts = build_graph(maze)
print('part 1:', get_all_keys(graph, starts, frozenset(graph.keys() - starts)))


maze[39][39 : 42] = list('@#@')
maze[40][39 : 42] = list('###')
maze[41][39 : 42] = list('@#@')

graph, starts = build_graph(maze)
print('part 2:', get_all_keys(graph, starts, frozenset(graph.keys() - starts)))
