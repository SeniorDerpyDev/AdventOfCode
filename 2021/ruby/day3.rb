input = File.readlines("../day_3.txt").map { |s| s.to_i(2) }
N_BITS = 12

gamma = 0
N_BITS.times do |n|
  gamma = gamma | (1 << n) if input.count { |i| i[n] == 1 } > input.length / 2.0
end
epsilon = 2**12 - 1 - gamma
print("part 1: ", gamma * epsilon, "\n")

def rating(list, n, what)
  return list[0] if list.length == 1
  ones = list.count { |i| i[n] == 1 }
  bit = ones >= list.length / 2.0 ? what : 1 - what
  rating(list.select { |i| i[n] == bit }, n-1, what)
end

oxygen, co2 = rating(input, N_BITS-1, 1), rating(input, N_BITS-1, 0)
print("part 2: ", oxygen * co2, "\n")

