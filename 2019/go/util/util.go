package util

func Abs(n int) int {
	if n < 0 {
		return -n
	}
	return n
}

func Min(a int, b int) int {
	if a > b {
		return b
	}
	return a
}
