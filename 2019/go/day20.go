package main

import (
	"AdventOfCode/util"
	"container/heap"
	"fmt"
)

const (
	inner = iota
	outer
)

var neighbours = [4]vec2{
	vec2{1, 0},
	vec2{-1, 0},
	vec2{0, -1},
	vec2{0, 1},
}

type vec2 struct {
	x int
	y int
}

type portal struct {
	name string
	side int
}

type node struct {
	portal
	dist int
}

type graph map[portal][]node

type item struct {
	portal portal
	dist   int
	level  int
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

func buildGraph(maze [][]byte) graph {
	portals := make(map[vec2]portal)
	height, width := len(maze), len(maze[0])
	for y, row := range maze {
		for x, c := range row {
			if c != '.' {
				continue
			}
			for _, n := range neighbours {
				c0 := maze[y+n.y][x+n.x]
				if c0 < 'A' || c0 > 'Z' {
					continue
				}

				c1 := maze[y+n.y+n.y][x+n.x+n.x]
				var name string
				if n.y > 0 || n.x > 0 {
					name = string(c0) + string(c1)
				} else {
					name = string(c1) + string(c0)
				}

				var side int
				if x == 2 || y == 2 || x == width-3 || y == height-3 {
					side = outer
				}

				portals[vec2{x, y}] = portal{name, side}
				break
			}
		}
	}

	type cell struct {
		vec   vec2
		steps int
	}
	g := make(graph)
	for vec, portal := range portals {
		var adjacent []node
		var queue []cell
		for _, n := range neighbours {
			nx, ny := vec.x+n.x, vec.y+n.y
			if maze[ny][nx] == '.' {
				queue = append(queue, cell{vec: vec2{nx, ny}, steps: 1})
			}
		}

		visited := make(map[vec2]bool)
		visited[vec] = true

		for len(queue) > 0 {
			c := queue[0]
			queue = queue[1:]

			if visited[c.vec] {
				continue
			}
			visited[c.vec] = true

			if p, ok := portals[c.vec]; ok {
				adjacent = append(adjacent, node{portal: p, dist: c.steps})
				continue
			}

			for _, n := range neighbours {
				nx, ny := c.vec.x+n.x, c.vec.y+n.y
				if maze[ny][nx] == '.' {
					queue = append(queue, cell{vec: vec2{nx, ny}, steps: c.steps + 1})
				}
			}
		}
		g[portal] = adjacent
	}
	return g
}

func walkMaze(g graph, start string, end string, rec bool) int {
	type visit struct {
		name  string
		side  int
		level int
	}

	visited := make(map[visit]bool)
	var q queue
	for _, node := range g[portal{start, outer}] {
		q = append(q, item{portal: node.portal, dist: node.dist, level: 0})
	}
	heap.Init(&q)
	for len(q) > 0 {
		it := heap.Pop(&q).(item)
		p := it.portal
		if p.name == end && it.level == 0 {
			return it.dist
		}

		v := visit{p.name, p.side, it.level}
		if visited[v] {
			continue
		}
		visited[v] = true

		out := portal{p.name, 1 - p.side}
		for _, node := range g[out] {
			l := it.level
			if rec {
				if p.side == outer {
					l = it.level - 1
				} else {
					l = it.level + 1
				}
			}
			if l >= 0 {
				heap.Push(&q, item{portal: node.portal, dist: 1 + it.dist + node.dist, level: l})
			}
		}
	}
	return -1
}

func main() {
	input, _ := util.ReadInput("../day_20.txt")
	maze := make([][]byte, len(input))
	for i, l := range input {
		maze[i] = []byte(l)
	}
	g := buildGraph(maze)
	fmt.Printf("part 1: %d\n", walkMaze(g, "AA", "ZZ", false))
	fmt.Printf("part 2: %d\n", walkMaze(g, "AA", "ZZ", true))
}
