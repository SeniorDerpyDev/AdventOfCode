require 'set'

inputs = File.readlines("../day_8.txt", chomp: true).map { |l| l.split(" | ") }
signals = inputs.map { |i| i[0].split }
numbers = inputs.map { |i| i[1].split }
segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
lookup = Hash.new
segments.each_with_index do |s,i|
  lookup[Set.new(s.chars)] = i
end

nice_lengths = [1,4,7,8].map { |d| segments[d].length }
print("part 1: ", numbers.sum { |n| n.count { |d| nice_lengths.include?(d.length) }}, "\n")

permutations = ('a'..'g').to_a.permutation.map &:join
total = 0
signals.each_with_index do |sig, i|
  permutations.each do |p|
    if sig.all? { |n| lookup.has_key?(Set.new(n.tr("abcdefg",p).chars)) }
      total += numbers[i].map { |n| lookup[Set.new(n.tr("abcdefg",p).chars)] }.join.to_i
      break
    end
  end
end
print("part 2: ", total, "\n")
