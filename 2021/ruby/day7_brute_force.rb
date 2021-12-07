crabs = File.read("../day_7.txt").split(",").map &:to_i

min, max = crabs.minmax
best1 = best2 = max*max*crabs.length
(min..max).each do |n|
  fuel = crabs.sum { |c| (c-n).abs }
  best1 = fuel if fuel < best1
  fuel = crabs.sum { |c| s=(c-n).abs; s*(s+1)/2 }
  best2 = fuel if fuel < best2
end

print("part 1: ", best1, "\n")
print("part 2: ", best2, "\n")
