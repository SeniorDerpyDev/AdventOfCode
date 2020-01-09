package main

import (
	"AdventOfCode/util"
	"fmt"
	"strings"
)

type orbit struct {
	center string
	level  int
}

var orbitsMap map[string]*orbit

func parse(lines []string) map[string]*orbit {
	orbits := make(map[string]*orbit)
	for _, l := range lines {
		objs := strings.Split(l, ")")
		orbits[objs[1]] = &orbit{
			center: objs[0],
			level:  -1,
		}
	}
	return orbits
}

func getLevel(obj string) int {
	if obj == "COM" {
		return 0
	}
	orbit := orbitsMap[obj]
	if orbit.level == -1 {
		orbit.level = getLevel(orbit.center) + 1
	}
	return orbit.level
}

func getOrbitedObjects(obj string) []string {
	result := make([]string, 0, orbitsMap[obj].level)
	for obj != "COM" {
		center := orbitsMap[obj].center
		result = append(result, center)
		obj = center
	}
	return result
}

func part1() int {
	total := 0
	for obj := range orbitsMap {
		total += getLevel(obj)
	}
	return total
}

func part2() int {
	you := getOrbitedObjects("YOU")
	santa := getOrbitedObjects("SAN")

	i := len(you) - 1
	j := len(santa) - 1
	for you[i] == santa[j] {
		i--
		j--
	}
	return i + 1 + j + 1
}

func main() {
	input, _ := util.ReadInput("../day_6.txt")
	orbitsMap = parse(input)

	fmt.Printf("part 1: %d\n", part1())
	fmt.Printf("part 2: %d\n", part2())
}
