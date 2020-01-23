package main

import (
	"AdventOfCode/util"
	"fmt"
	"io/ioutil"
	"strconv"
)

func getSignal(data []byte) []int {
	signal := make([]int, len(data))
	for i, b := range data {
		signal[i] = int(b - '0')
	}
	return signal
}

func part1(signal []int, phases int) []int {
	l := len(signal)
	for p := 0; p < phases; p++ {
		next := make([]int, l)
		for i := 0; i < l; i++ {
			j, d, total := i, i+1, 0
			for j < l {
				for k := j; k < j+d && k < l; k++ {
					total += signal[k]
				}
				j += d + d
				for k := j; k < j+d && k < l; k++ {
					total -= signal[k]
				}
				j += d + d
			}
			next[i] = util.Abs(total) % 10
		}
		signal = next
	}
	return signal[:8]
}

func part2(signal []int, phases int, offset int) []int {
	l := len(signal)
	realSignal := make([]int, l*10000-offset)
	rl := len(realSignal)

	n := rl - l
	for ; n > 0; n -= l {
		copy(realSignal[n:n+l], signal)
	}
	copy(realSignal[0:n+l], signal[-n:])

	for p := 0; p < phases; p++ {
		sum := 0
		for i := rl - 1; i >= 0; i-- {
			sum += realSignal[i]
			realSignal[i] = sum % 10
		}
	}
	return realSignal[:8]
}

func main() {
	input, _ := ioutil.ReadFile("../day_16.txt")
	signal := getSignal(input[0 : len(input)-2])

	fmt.Printf("part 1: %v\n", part1(signal, 100))
	offset, _ := strconv.Atoi(string(input[0:7]))
	fmt.Printf("part 2: %v\n", part2(signal, 100, offset))
}
