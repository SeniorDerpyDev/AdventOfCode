package main

import (
	"AdventOfCode/util"
	"fmt"
	"math/big"
	"strconv"
	"strings"
)

const (
	cut = iota
	dealNew
	dealInc
)

type shuffle struct {
	technique int
	num       int
}

func parse(lines []string) []shuffle {
	s := make([]shuffle, len(lines))
	for i, l := range lines {
		if strings.HasPrefix(l, "cut ") {
			n, _ := strconv.Atoi(l[4:])
			s[i].technique = cut
			s[i].num = n
		} else if strings.HasPrefix(l, "deal with increment ") {
			n, _ := strconv.Atoi(l[20:])
			s[i].technique = dealInc
			s[i].num = n
		} else if strings.HasPrefix(l, "deal into new stack") {
			s[i].technique = dealNew
		}
	}
	return s
}

func linearTransf(shuffles []shuffle, mod *big.Int) (*big.Int, *big.Int) {
	a, b := big.NewInt(1), big.NewInt(0)
	for _, s := range shuffles {
		num := big.NewInt(int64(s.num))
		switch s.technique {
		case cut:
			b.Sub(b, num).Mod(b, mod)
		case dealNew:
			a.Neg(a).Mod(a, mod)
			b.Sub(mod, b).Sub(b, big.NewInt(1))
		case dealInc:
			a.Mul(a, num).Mod(a, mod)
			b.Mul(b, num).Mod(b, mod)
		}
	}
	return a, b
}

func part1(shuffles []shuffle) int64 {
	const nCards = 10007
	mod := big.NewInt(int64(nCards))
	a, b := linearTransf(shuffles, mod)
	r := new(big.Int)
	r.Mul(a, big.NewInt(2019)).Add(r, b).Mod(r, mod)
	return r.Int64()
}

func part2(shuffles []shuffle) int64 {
	const (
		nCards = 119315717514047
		nTimes = 101741582076661
	)
	mod, exp, one := big.NewInt(int64(nCards)), big.NewInt(int64(nTimes)), big.NewInt(1)
	a, b := linearTransf(shuffles, mod)

	// inverse transformation
	a.ModInverse(a, mod)
	b.Neg(b).Mul(a, b).Mod(b, mod)

	// compose nTimes
	ca, cb := new(big.Int), new(big.Int)
	ca.Exp(a, exp, mod)
	cb.Sub(ca, one).Mul(cb, b)
	a.Sub(a, one).ModInverse(a, mod)
	cb.Mul(cb, a)

	r := new(big.Int)
	r.Mul(ca, big.NewInt(2020)).Add(r, cb).Mod(r, mod)
	return r.Int64()
}

func main() {
	input, _ := util.ReadInput("../day_22.txt")
	shuffles := parse(input)
	fmt.Printf("part 1: %d\n", part1(shuffles))
	fmt.Printf("part 2: %d\n", part2(shuffles))
}
