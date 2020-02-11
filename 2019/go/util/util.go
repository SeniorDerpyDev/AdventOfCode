package util

import (
	"bufio"
	"os"
)

// ReadInput returns a slice of strings containing all the lines in the file
func ReadInput(file string) ([]string, error) {
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
	return input, scanner.Err()
}

// Abs returns the absolute value of n.
func Abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

// Max returns the larger of a or b.
func Max(a int, b int) int {
	if a < b {
		return b
	}
	return a
}

// Min returns the smaller of a or b.
func Min(a int, b int) int {
	if a > b {
		return b
	}
	return a
}

// Gcd returns the greatest common divisor of a and b.
func Gcd(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

// Lcm returns the least common multiple of a and b.
func Lcm(a int, b int) int {
	return a * b / Gcd(a, b)
}
