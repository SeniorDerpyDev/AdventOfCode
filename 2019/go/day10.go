package main

import (
	"AdventOfCode/util"
	"fmt"
	"math"
	"sort"
)

type asteroidMap = [][]bool

type point struct {
	x int
	y int
}

var asteroids asteroidMap

func parse(lines []string) [][]bool {
	result := make(asteroidMap, len(lines))
	for y, line := range lines {
		result[y] = make([]bool, len(line))
		for x, c := range line {
			if c == '#' {
				result[y][x] = true
			}
		}
	}
	return result
}

func getVisible(x int, y int) []point {
	visible := make([]point, 0)
	for y1, row := range asteroids {
		for x1 := range row {
			dx, dy := x1-x, y1-y
			if util.Abs(util.Gcd(dx, dy)) == 1 {
				for tx, ty := x+dx, y+dy; tx >= 0 && ty >= 0 && tx < len(row) && ty < len(asteroids); tx, ty = tx+dx, ty+dy {
					if asteroids[ty][tx] {
						visible = append(visible, point{tx, ty})
						break
					}
				}
			}
		}
	}
	return visible
}

func part1() (point, []point) {
	var best []point
	var bestX, bestY int
	for y, row := range asteroids {
		for x, a := range row {
			if a {
				visible := getVisible(x, y)
				if len(visible) > len(best) {
					best = visible
					bestX, bestY = x, y
				}
			}
		}
	}
	return point{bestX, bestY}, best
}

func angle(a point, b point) float64 {
	return math.Atan2(float64(b.x-a.x), float64(b.y-a.y))
}

func part2(asteroid point, visible []point) int {
	sortFunc := func(i, j int) bool {
		return angle(asteroid, visible[i]) > angle(asteroid, visible[j])
	}
	sort.Slice(visible, sortFunc)
	target := visible[199]
	return target.x*100 + target.y
}

func main() {
	input, _ := util.ReadInput("../day_10.txt")
	asteroids = parse(input)

	asteroid, visible := part1()
	fmt.Printf("part 1: %d\n", len(visible))
	fmt.Printf("part 2: %d\n", part2(asteroid, visible))
}
