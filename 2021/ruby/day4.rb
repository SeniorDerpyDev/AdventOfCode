require 'set'

input = File.read('../day_4.txt').split("\n\n")
rng = input.shift.split(",").map &:to_i
boards = input.map do |b|
  board = { :cols => Array.new(5) {Set.new}, :rows => Array.new(5) {Set.new} }
  b.split.map(&:to_i).each_with_index { |n, idx|
    board[:cols][idx%5].add(n)
    board[:rows][idx/5].add(n)
  }
  board
end

def run(rng, boards)
  rng.each do |n|
    boards.each do |b|
      b[:cols].each { |c| c.delete(n); yield [b, n] if c.empty? }
      b[:rows].each { |r| r.delete(n); yield [b, n] if r.empty? }
    end
    boards = boards.reject { |b| b[:cols].any?(&:empty?) || b[:rows].any?(&:empty?) }
  end
end

bingos = []
run(rng, boards) { |r| bingos << r }

board, n = bingos.first
print("part 1: ", n*board[:cols].sum { |c| c.sum }, "\n")
board, n = bingos.last
print("part 2: ", n*board[:cols].sum { |c| c.sum }, "\n")
