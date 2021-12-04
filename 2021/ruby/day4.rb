require 'set'

input = File.read('../day_4.txt').split("\n\n")
rng = input.shift.split(",").map &:to_i
boards = input.collect do |b|
  board = { :cols => Array.new(5) {Set.new}, :rows => Array.new(5) {Set.new} }
  b.split().map(&:to_i).each_with_index { |n, idx|
    board[:cols][idx%5].add(n)
    board[:rows][idx/5].add(n)
  }
  board
end

def run1(rng, boards)
  rng.each do |n|
    boards.each do |b|
      b[:cols].each { |c| c.delete(n); return [b, n] if c.empty? }
      b[:rows].each { |r| r.delete(n); return [b, n] if r.empty? }
    end
  end
end

bingo, n = run1(rng, boards)
print("part 1: ", n*bingo[:cols].collect { |c| c.each.sum }.sum, "\n")

def run2(rng, boards)
  rng.each do |n|
    boards.each do |b|
      b[:cols].each { |c| c.delete(n); return [b, n] if c.empty? and boards.length == 1 }
      b[:rows].each { |r| r.delete(n); return [b, n] if r.empty? and boards.length == 1 }
    end
    boards = boards.reject { |b| b[:cols].any? &:empty? }.reject { |b| b[:rows].any? &:empty? }
  end
end

bingo, n = run2(rng, boards)
print("part 2: ", n*bingo[:cols].collect { |c| c.each.sum }.sum, "\n")
