package main

import (
	"AdventOfCode/util"
	"fmt"
	"regexp"
	"strconv"
)

const (
	xAxis = iota
	yAxis
	zAxis
)

type vector = [3]int

type moon struct {
	position vector
	velocity vector
}

var intRegex = regexp.MustCompile(`-?\d+`)

func parse(lines []string) []moon {
	moons := make([]moon, len(lines))
	for i, l := range lines {
		for j, s := range intRegex.FindAllString(l, -1) {
			num, _ := strconv.Atoi(s)
			moons[i].position[j] = num
		}
	}
	return moons
}

func step(moons []moon) {
	for i := 0; i < len(moons)-1; i++ {
		for j := i; j < len(moons); j++ {
			for d := 0; d < 3; d++ {
				switch cmp := moons[i].position[d] - moons[j].position[d]; {
				case cmp < 0:
					moons[i].velocity[d]++
					moons[j].velocity[d]--
				case cmp > 0:
					moons[i].velocity[d]--
					moons[j].velocity[d]++
				}
			}
		}
	}

	for i := 0; i < len(moons); i++ {
		for d := 0; d < 3; d++ {
			moons[i].position[d] += moons[i].velocity[d]
		}
	}
}

func energy(moons []moon) int {
	var e int
	for i := 0; i < len(moons); i++ {
		var pe, ke int
		for d := 0; d < 3; d++ {
			pe += util.Abs(moons[i].position[d])
			ke += util.Abs(moons[i].velocity[d])
		}
		e += pe * ke
	}
	return e
}

func findPeriod(moons []moon, axis int) int {
	m := make([]moon, len(moons))
	copy(m, moons)

	p := 0
	equal := false
	for !equal {
		p++
		step(m)

		equal = true
		for i := 0; i < len(moons); i++ {
			if m[i].position[axis] != moons[i].position[axis] ||
				m[i].velocity[axis] != moons[i].velocity[axis] {
				equal = false
				break
			}
		}
	}
	return p
}

func part1(moons []moon) int {
	for i := 0; i < 1000; i++ {
		step(moons)
	}
	return energy(moons)
}

func part2(moons []moon) int {
	px := findPeriod(moons, xAxis)
	py := findPeriod(moons, yAxis)
	pz := findPeriod(moons, zAxis)
	return util.Lcm(px, util.Lcm(py, pz))
}

func main() {
	input, _ := util.ReadInput("../day_12.txt")
	moons := parse(input)

	fmt.Printf("part 1: %d\n", part1(moons))
	fmt.Printf("part 2: %d\n", part2(moons))
}
