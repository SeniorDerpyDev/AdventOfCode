package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readInput(file string) ([]int, error) {
	f, err := os.Open(file)
	if err != nil {
		return nil, err
	}
	defer f.Close()

	var input []int
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		var n int
		if n, err = strconv.Atoi(scanner.Text()); err != nil {
			return nil, err
		}
		input = append(input, n)
	}
	return input, err
}

func fuel(mass int) int {
	f := mass/3 - 2
	if f <= 0 {
		return 0
	}
	return f + fuel(f)
}

func main() {
	modules, _ := readInput("../day_1.txt")
	total1, total2 := 0, 0
	for _, m := range modules {
		total1 += m/3 - 2
		total2 += fuel(m)
	}
	fmt.Printf("part 1: %d\n", total1)
	fmt.Printf("part 2: %d\n", total2)
}
