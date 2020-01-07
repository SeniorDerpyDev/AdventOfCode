package main

import (
	"AdventOfCode/intcode"
	"AdventOfCode/util"
	"fmt"
)

func part1(pgm string) int {
	computer, _ := intcode.LoadProgram(pgm)
	computer.Mem[1] = 12
	computer.Mem[2] = 2
	computer.Run()
	return computer.Mem[0]
}

func part2(pgm string, expected int) int {
	for noun := 0; noun < 100; noun++ {
		for verb := 0; verb < 100; verb++ {
			computer, _ := intcode.LoadProgram(pgm)
			computer.Mem[1] = noun
			computer.Mem[2] = verb
			computer.Run()
			if computer.Mem[0] == expected {
				return noun*100 + verb
			}
		}
	}
	return -1
}

func main() {
	input, _ := util.ReadInput("../day_2.txt")
	pgm := input[0]
	fmt.Printf("part 1: %d\n", part1(pgm))
	fmt.Printf("part 2: %d\n", part2(pgm, 19690720))
}
