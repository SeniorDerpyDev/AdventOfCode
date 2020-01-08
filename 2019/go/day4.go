package main

import (
	"AdventOfCode/util"
	"fmt"
	"strconv"
	"strings"
)

func parse(s string) (int, int) {
	pwdRange := strings.Split(s, "-")
	begin, _ := strconv.Atoi(pwdRange[0])
	end, _ := strconv.Atoi(pwdRange[1])
	return begin, end
}

func countPasswords(b int, e int) (int, int) {
	count1, count2 := 0, 0
	for n := b; n < e; n++ {
		p := strconv.Itoa(n)
		decreases, adjacentEq, double := false, false, false
		consecutive := 1
		for i := 0; i < 5; i++ {
			if p[i] > p[i+1] {
				decreases = true
				break
			} else if p[i] == p[i+1] {
				adjacentEq = true
				consecutive++
			} else {
				if consecutive == 2 {
					double = true
				}
				consecutive = 1
			}
		}
		if consecutive == 2 {
			double = true
		}

		if adjacentEq && !decreases {
			count1++
			if double {
				count2++
			}
		}
	}
	return count1, count2
}

func main() {
	input, _ := util.ReadInput("../day_4.txt")
	b, e := parse(input[0])

	part1, part2 := countPasswords(b, e)
	fmt.Printf("part 1: %d\n", part1)
	fmt.Printf("part 2: %d\n", part2)
}
