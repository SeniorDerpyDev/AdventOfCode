package aoc2020

import java.io.File

fun helper(input: List<Int>, target: Int): Int {
	var b = 0
	var e = input.size-1

	while (b < e) {
		val s = input[b] + input[e]
		when {
			s == target -> return input[b] * input[e]
			s < target -> b += 1
			else -> e -= 1
		}
	}
	return -1
}

fun part1(input: List<Int>, target: Int): Int {
	return helper(input, target)
}

fun part2(input: List<Int>, target: Int): Int {
	for (i in 0..input.size-1) {
		val n = input[i]
		val m = helper(input.subList(i+1, input.size), target - n)
		if (m > 0) return n*m
	}
	return -1
}

fun main() {
	val l = File("../day_1.txt").readLines().map(String::toInt).sorted()
	println("Part 1: ${part1(l, 2020)}")
	println("Part 2: ${part2(l, 2020)}")
}
