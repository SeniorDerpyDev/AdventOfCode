crabs = File.read("../day_7.txt").split(",").map &:to_i
crabs.sort!

# The median minimizes sum of absolute deviations
median = crabs[crabs.length/2]
print("part 1: ", crabs.sum { |x| (x-median).abs }, "\n")

# The mean minimizes sum of squared deviations
mean = crabs.sum / crabs.length
print("part 2: ", crabs.sum { |x| s=(x-mean).abs; s*(s+1)/2 }, "\n")
