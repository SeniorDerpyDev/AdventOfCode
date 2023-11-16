require 'set'

entries = File.readlines("../day_8.txt", chomp: true).map { |l| l.split(" | ").map &:split }
segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
lookup = Hash.new
segments.each_with_index do |s,i|
  lookup[Set.new(s.chars)] = i
end

print("part 1: ", entries.sum { |_, nums| nums.count { |d| [2,3,4,7].include?(d.length) }}, "\n")

permutations = ('a'..'g').to_a.permutation.map &:join
total = 0
entries.each do |sigs, nums|
  permutations.each do |p|
    if sigs.all? { |s| lookup.has_key?(Set.new(s.tr("abcdefg",p).chars)) }
      total += nums.map { |n| lookup[Set.new(n.tr("abcdefg",p).chars)] }.join.to_i
      break
    end
  end
end
print("part 2: ", total, "\n")
