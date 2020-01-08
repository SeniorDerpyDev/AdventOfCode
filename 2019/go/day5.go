package main

import (
	"AdventOfCode/intcode"
	"AdventOfCode/util"
	"fmt"
)

func part1(pgm string) int {
	computer, _ := intcode.LoadProgram(pgm)
	computer.Verbose(true)
	computer.Write(1)
	computer.Run()
	return computer.Read()
}

func part2(pgm string) int {
	computer, _ := intcode.LoadProgram(pgm)
	computer.Write(5)
	computer.Run()
	return computer.Read()
}

func main() {
	input, _ := util.ReadInput("../day_5.txt")
	pgm := input[0]
	fmt.Printf("part 1: %d\n", part1(pgm))
	fmt.Printf("part 2: %d\n", part2(pgm))
}
