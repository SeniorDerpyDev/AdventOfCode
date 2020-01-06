from collections import defaultdict, deque

adjacent = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def maze_info(txt, top_left=None, bottom_right=None):
	x0, y0 = top_left if top_left else (0, 0)
	x1, y1 = bottom_right if bottom_right else (len(maze[0]), len(maze))
	start = (None, None)
	keys = set()
	for y in range(y0, y1):
		for x in range(x0, x1):
			c = maze[y][x]
			if c == '@':
				start = (x, y) 
			if 'a' <= c <= 'z':
				keys.add(c)
	return start, keys

def get_all_keys(maze, start, all_keys):
	cells = deque([(*start, '', 0)])
	visited = defaultdict(set)

	while cells:
		(x, y, keys_found, steps) = cells.popleft()
		c = maze[y][x] 

		if c == '#':
			continue		
		if (x, y) in visited[frozenset(keys_found)]:
			continue
		if 'A' <= c <= 'Z':
			door = c.lower()
			if door in all_keys and door not in keys_found:
				continue

		if 'a' <= c <= 'z' and c not in keys_found:
			keys_found += c
			if set(keys_found) == all_keys:
				return steps
		
		cells.extend([(x + dx, y + dy, keys_found, steps + 1) for (dx, dy) in adjacent])
		visited[frozenset(keys_found)].add((x, y))

with open('../day_18.txt', 'r') as f:
	maze = [list(line) for line in f.read().splitlines()]

print('part 1:', get_all_keys(maze, *maze_info(maze)))

maze[39][39 : 42] = list('@#@')
maze[40][39 : 42] = list('###')
maze[41][39 : 42] = list('@#@')

s1 = get_all_keys(maze, *maze_info(maze, (0, 0), (41, 41)))
s2 = get_all_keys(maze, *maze_info(maze, (40, 0), (81, 41)))
s3 = get_all_keys(maze, *maze_info(maze, (0, 40), (41, 81)))
s4 = get_all_keys(maze, *maze_info(maze, (40, 40), (81, 81)))
print('part 2:', s1 + s2 + s3 + s4)
