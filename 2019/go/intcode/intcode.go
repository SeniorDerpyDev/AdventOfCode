package intcode

import (
	"fmt"
	"strconv"
	"strings"
)

const (
	rd = iota
	wr = iota
)

const (
	pos   = iota
	immed = iota
)

var opCodeParms = map[int][]int{
	1:  {rd, rd, wr},
	2:  {rd, rd, wr},
	3:  {wr},
	4:  {rd},
	5:  {rd, rd},
	6:  {rd, rd},
	7:  {rd, rd, wr},
	8:  {rd, rd, wr},
	99: {},
}

type Intcode struct {
	ip      int
	opCode  int
	regs    [3]int
	input   int
	output  int
	Halt    bool
	verbose bool
	Mem     []int
}

func LoadProgram(pgm string) (*Intcode, error) {
	result := Intcode{}
	values := strings.Split(pgm, ",")
	result.Mem = make([]int, len(values))
	for i, str := range values {
		if v, err := strconv.Atoi(str); err == nil {
			result.Mem[i] = v
		} else {
			return nil, fmt.Errorf("invalid program, %v is not an int. %w", v, err)
		}
	}
	return &result, nil
}

func (c *Intcode) loadRegs() {
	c.opCode = c.Mem[c.ip]
	c.ip++
	modes := c.opCode / 100
	c.opCode = c.opCode % 100

	parms := opCodeParms[c.opCode]
	for i, p := range parms {
		mode := modes % 10
		modes = modes / 10
		v := c.Mem[c.ip]
		c.ip++
		if p == rd {
			if mode == immed {
				c.regs[i] = v
			} else {
				c.regs[i] = c.Mem[v]
			}
		} else {
			c.regs[i] = v
		}
	}
}

func (c *Intcode) step() {
	c.loadRegs()
	switch c.opCode {
	case 1:
		c.Mem[c.regs[2]] = c.regs[0] + c.regs[1]
	case 2:
		c.Mem[c.regs[2]] = c.regs[0] * c.regs[1]
	case 3:
		c.Mem[c.regs[0]] = c.input
	case 4:
		c.output = c.regs[0]
		if c.verbose {
			fmt.Println(c.output)
		}
	case 5:
		if c.regs[0] != 0 {
			c.ip = c.regs[1]
		}
	case 6:
		if c.regs[0] == 0 {
			c.ip = c.regs[1]
		}
	case 7:
		if c.regs[0] < c.regs[1] {
			c.Mem[c.regs[2]] = 1
		} else {
			c.Mem[c.regs[2]] = 0
		}
	case 8:
		if c.regs[0] == c.regs[1] {
			c.Mem[c.regs[2]] = 1
		} else {
			c.Mem[c.regs[2]] = 0
		}
	case 99:
		c.Halt = true
	}
}

func (c *Intcode) Run() {
	for !c.Halt {
		c.step()
	}
}

func (c *Intcode) Read() int {
	return c.output
}

func (c *Intcode) Write(value int) {
	c.input = value
}

func (c *Intcode) Verbose(value bool) {
	c.verbose = value
}

func (c *Intcode) DumpMemory() string {
	var b strings.Builder
	b.WriteString(strconv.Itoa(c.Mem[0]))
	for _, v := range c.Mem[1:] {
		b.WriteString(",")
		b.WriteString(strconv.Itoa(v))
	}
	return b.String()
}
