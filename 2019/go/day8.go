package main

import (
	"fmt"
	"io/ioutil"
	"math"
)

const width = 25
const height = 6
const size = width * height

func part1(data []byte) int {
	result := 0
	current := math.MaxInt64

	for i := 0; i < len(data); i += size {
		totals := make(map[byte]int)
		for j := i; j < i+size; j++ {
			totals[data[j]]++
		}
		if totals['0'] < current {
			current = totals['0']
			result = totals['1'] * totals['2']
		}
	}
	return result
}

func part2(data []byte) string {
	var img [size]byte

	nLayers := len(data) / size
	for i := nLayers; i >= 0; i-- {
		layer := data[i*size : (i+1)*size]
		for j := 0; j < size; j++ {
			switch layer[j] {
			case '0':
				img[j] = ' '
			case '1':
				img[j] = '#'
			}
		}
	}

	var result string
	for n := 0; n < size; n += width {
		result += string(img[n:n+width]) + "\n"
	}
	return result
}

func main() {
	input, _ := ioutil.ReadFile("../day_8.txt")
	input = input[0 : len(input)-2] // remove \r\n

	fmt.Printf("part 1: %d\n", part1(input))
	fmt.Printf("part 2:\n%s", part2(input))
}
