package main

import (
	"AdventOfCode/util"
	"container/heap"
	"fmt"
)

var neighbours = [4]point{
	point{1, 0},
	point{-1, 0},
	point{0, -1},
	point{0, 1},
}

type point struct {
	x int
	y int
}

type node struct {
	key   byte
	dist  int
	doors int
}

type graph map[byte][]node

type item struct {
	nodes     []byte
	dist      int
	collected int
}

type queue []item

func (q queue) Len() int { return len(q) }

func (q queue) Less(i, j int) bool {
	return q[i].dist < q[j].dist
}

func (q queue) Swap(i, j int) {
	q[i], q[j] = q[j], q[i]
}

func (q *queue) Push(x interface{}) {
	i := x.(item)
	*q = append(*q, i)
}

func (q *queue) Pop() interface{} {
	old := *q
	n := len(old)
	i := old[n-1]
	*q = old[0 : n-1]
	return i
}

func bytesToInt(bs []byte) int {
	var r, s int
	for _, b := range bs {
		r |= int(b) << s
		s += 8
	}
	return r
}

func isStart(char byte) bool {
	return char == '@' || (char >= '1' && char <= '4')
}

func isKey(char byte) bool {
	return char >= 'a' && char <= 'z'
}

func isDoor(char byte) bool {
	return char >= 'A' && char <= 'Z'
}

func keyToBits(char byte) int {
	return 1 << (char - 'a')
}

func doorToBits(char byte) int {
	return 1 << (char - 'A')
}

func buildGraph(maze [][]byte) (graph, int) {
	g := make(graph)
	keys := 0
	for y, row := range maze {
		for x, c := range row {
			if isKey(c) {
				keys |= keyToBits(c)
				g[byte(c)] = getAdjacentNodes(maze, x, y)
			} else if isStart(c) {
				g[byte(c)] = getAdjacentNodes(maze, x, y)
			}
		}
	}
	return g, keys
}

func getAdjacentNodes(maze [][]byte, x int, y int) []node {
	type cell struct {
		point
		steps int
		doors int
	}

	var adjacent []node
	var queue []cell
	for _, n := range neighbours {
		nx, ny := x+n.x, y+n.y
		if maze[ny][nx] != '#' {
			queue = append(queue, cell{point: point{nx, ny}, steps: 1})
		}
	}

	visited := make(map[point]bool)
	visited[point{x, y}] = true

	for len(queue) > 0 {
		c := queue[0]
		queue = queue[1:]

		if visited[point{c.x, c.y}] {
			continue
		}
		visited[point{c.x, c.y}] = true

		char := maze[c.y][c.x]
		if isKey(char) {
			adjacent = append(adjacent, node{key: char, dist: c.steps, doors: c.doors})
			continue
		}
		if isDoor(char) {
			c.doors |= doorToBits(char)
		}

		for _, n := range neighbours {
			nx, ny := c.x+n.x, c.y+n.y
			if maze[ny][nx] != '#' {
				queue = append(queue, cell{point: point{nx, ny}, steps: c.steps + 1, doors: c.doors})
			}
		}
	}
	return adjacent
}

func collectKeys(g graph, starts []byte, allKeys int) int {
	type visit struct {
		nodes     int
		collected int
	}

	visited := make(map[visit]bool)
	q := queue{item{nodes: starts, dist: 0, collected: 0}}
	heap.Init(&q)

	for len(q) > 0 {
		it := heap.Pop(&q).(item)
		if it.collected == allKeys {
			return it.dist
		}
		v := visit{bytesToInt(it.nodes), it.collected}
		if visited[v] {
			continue
		}
		visited[v] = true

		for j, node := range it.nodes {
			for _, next := range g[node] {
				if next.doors&it.collected == next.doors {
					nodes := make([]byte, len(it.nodes))
					copy(nodes, it.nodes)
					nodes[j] = next.key
					heap.Push(&q, item{nodes: nodes, dist: it.dist + next.dist, collected: it.collected | keyToBits(next.key)})
				}
			}
		}
	}
	return -1
}

func main() {
	input, _ := util.ReadInput("../day_18.txt")
	maze := make([][]byte, len(input))
	for i, l := range input {
		maze[i] = []byte(l)
	}
	graph, keys := buildGraph(maze)
	fmt.Printf("part 1: %d\n", collectKeys(graph, []byte{'@'}, keys))

	maze[39][39], maze[39][40], maze[39][41] = '1', '#', '2'
	maze[40][39], maze[40][40], maze[40][41] = '#', '#', '#'
	maze[41][39], maze[41][40], maze[41][41] = '4', '#', '3'
	graph, keys = buildGraph(maze)
	fmt.Printf("part 2: %d\n", collectKeys(graph, []byte{'1', '2', '3', '4'}, keys))
}
