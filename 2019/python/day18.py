from heapq import heappop, heappush

neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def build_graph(maze, starts):
    graph = dict()
    for y, row in enumerate(maze):
        for x, c in enumerate(row):
            if 'a' <= c <= 'z' or c in starts:
                graph[c] = find_adjacent(maze, (x, y))
    return graph

def find_adjacent(maze, start):
    visited = {start}
    adjacent = []
    x, y = start
    cells = [(x+dx, y+dy, 1, set()) for (dx, dy) in neighbours if maze[y+dy][x+dx] != '#']

    while cells:
        (x, y, steps, doors) = cells.pop(0)
        if (x, y) in visited:
            continue
        visited.add((x, y))

        c = maze[y][x]
        if 'a' <= c <= 'z':
            adjacent.append((c, steps, doors))
            continue
        if 'A' <= c <= 'Z':
            doors = doors | {c.lower()}

        cells.extend([(x+dx, y+dy, steps + 1, doors) for (dx, dy) in neighbours if maze[y+dy][x+dx] != '#'])
    return adjacent

def get_all_keys(g, starts, keys_to_collect):
    q = []
    heappush(q, (0, starts, frozenset()))
    visited = set()

    while q:
        (steps, nodes, keys) = heappop(q)
        if keys == keys_to_collect:
            return steps
        if (nodes, keys) in visited:
            continue
        for n in nodes:
            for next, dist, doors in g[n]:
                if doors.issubset(keys):
                    heappush(q, (steps + dist, nodes.replace(n, next), keys | {next}))

        visited.add((nodes, keys))

with open('../day_18.txt', 'r') as f:
    maze = [list(line) for line in f.read().splitlines()]

starts = '@'
graph = build_graph(maze, starts)
print('part 1:', get_all_keys(graph, starts, frozenset(graph.keys() - starts)))


maze[39][39 : 42] = list('1#2')
maze[40][39 : 42] = list('###')
maze[41][39 : 42] = list('4#3')

starts = '1234'
graph = build_graph(maze, starts)
print('part 2:', get_all_keys(graph, starts, frozenset(graph.keys() - starts)))
