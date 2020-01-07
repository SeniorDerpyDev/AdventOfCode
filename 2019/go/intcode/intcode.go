package intcode

import (
	"fmt"
	"strconv"
	"strings"
)

type Intcode struct {
	Halt bool
	Mem  []int
	ip   int
}

func LoadProgram(pgm string) (*Intcode, error) {
	result := Intcode{}
	opcodes := strings.Split(pgm, ",")
	result.Mem = make([]int, len(opcodes))
	for i, str := range opcodes {
		if opcode, err := strconv.Atoi(str); err == nil {
			result.Mem[i] = opcode
		} else {
			fmt.Printf("%v\n", err)
			return nil, fmt.Errorf("invalid opcode: %v. %w", opcode, err)
		}
	}
	return &result, nil
}

func (computer *Intcode) step() {
	ip := computer.ip
	opcode := computer.Mem[ip]
	a, b, c := computer.Mem[ip+1], computer.Mem[ip+2], computer.Mem[ip+3]
	switch opcode {
	case 1:
		computer.Mem[c] = computer.Mem[a] + computer.Mem[b]
	case 2:
		computer.Mem[c] = computer.Mem[a] * computer.Mem[b]
	case 99:
		computer.Halt = true
	}
	computer.ip += 4
}

func (computer *Intcode) Run() {
	for !computer.Halt {
		computer.step()
	}
}

func (computer *Intcode) DumpMemory() string {
	var b strings.Builder
	b.WriteString(strconv.Itoa(computer.Mem[0]))
	for _, v := range computer.Mem[1:] {
		b.WriteString(",")
		b.WriteString(strconv.Itoa(v))
	}
	return b.String()
}
