package main

import (
	"AdventOfCode/util"
	"bufio"
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type point struct {
	x int
	y int
}

type wire = map[point]int

func readInput(file string) ([]string, error) {
	f, err := os.Open(file)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	var input []string
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		input = append(input, scanner.Text())
	}
	return input, err
}

func parse(s string) wire {
	result := make(wire)
	segments := strings.Split(s, ",")
	p := point{}
	steps := 0
	for _, seg := range segments {
		dir := seg[0]
		len, _ := strconv.Atoi(seg[1:])
		for i := 0; i < len; i++ {
			switch dir {
			case 'U':
				p.y--
			case 'D':
				p.y++
			case 'L':
				p.x--
			case 'R':
				p.x++
			}
			steps++
			if _, ok := result[p]; !ok {
				result[p] = steps
			}
		}
	}
	return result
}

func part1(wire0 wire, wire1 wire) int {
	result := math.MaxInt64
	for p := range wire0 {
		if _, ok := wire1[p]; ok {
			result = util.Min(result, util.Abs(p.x)+util.Abs(p.y))
		}
	}
	return int(result)
}

func part2(wire0 wire, wire1 wire) int {
	result := math.MaxInt64
	for p, s0 := range wire0 {
		if s1, ok := wire1[p]; ok {
			result = util.Min(result, s0+s1)
		}
	}
	return int(result)
}

func main() {
	paths, _ := readInput("../day_3.txt")
	wire0 := parse(paths[0])
	wire1 := parse(paths[1])

	fmt.Printf("part 1: %d\n", part1(wire0, wire1))
	fmt.Printf("part 2: %d\n", part2(wire0, wire1))
}
