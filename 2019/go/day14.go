package main

import (
	"AdventOfCode/util"
	"fmt"
	"math"
	"strconv"
	"strings"
)

type reagent struct {
	name string
	qty  int
}

type reaction struct {
	qty      int
	reagents []reagent
}

var reactions map[string]reaction
var chemicals []string

func parseChemical(s string) (int, string) {
	values := strings.Split(s, " ")
	if n, err := strconv.Atoi(values[0]); err == nil {
		return n, values[1]
	}
	return 0, ""
}

func parse(lines []string) map[string]reaction {
	reactions := make(map[string]reaction)
	for _, l := range lines {
		sides := strings.Split(l, " => ")

		// inputs
		inputs := strings.Split(sides[0], ", ")
		reagents := make([]reagent, len(inputs))
		for i, input := range inputs {
			qty, chem := parseChemical(input)
			reagents[i].name = chem
			reagents[i].qty = qty
		}

		// output
		qty, chem := parseChemical(sides[1])
		reactions[chem] = reaction{
			qty,
			reagents,
		}
	}
	return reactions
}

func getChemicalsInOrder() []string {
	var aux func(string)
	var result []string

	visited := make(map[string]bool)
	aux = func(c string) {
		visited[c] = true
		for _, reagent := range reactions[c].reagents {
			if !visited[reagent.name] {
				aux(reagent.name)
			}
		}
		result = append(result, c)
	}

	for chem := range reactions {
		if !visited[chem] {
			aux(chem)
		}
	}
	return result
}

func getOreQty(fuel int) int {
	required := make(map[string]int)
	required["FUEL"] = fuel
	for i := len(chemicals) - 1; i >= 0; i-- {
		chem := chemicals[i]
		req := required[chem]
		reaction := reactions[chem]
		m := int(math.Ceil(float64(req) / float64(reaction.qty)))
		for _, reagent := range reaction.reagents {
			required[reagent.name] += m * reagent.qty
		}
	}
	return required["ORE"]
}

func part1() int {
	return getOreQty(1)
}

func part2() int {
	min := 1e12 / getOreQty(1)
	max := 2 * min

	for min < max {
		mid := (max+min)/2 + 1
		ore := getOreQty(mid)
		if ore > 1e12 {
			max = mid - 1
		} else {
			min = mid
		}
	}
	return min
}

func main() {
	input, _ := util.ReadInput("../day_14.txt")
	reactions = parse(input)
	chemicals = getChemicalsInOrder()

	fmt.Printf("part 1: %d\n", part1())
	fmt.Printf("part 2: %d\n", part2())
}
