fish = [0] * 9
File.read("../day_6.txt").split(",").map(&:to_i).each { |f| fish[f.to_i] += 1 }

def simulate(n, fish)
  n.times do
    fish.rotate!
    fish[6] += fish[8]
  end
  fish.sum
end

print("part 1: ", simulate(80, fish.dup), "\n")
print("part 2: ", simulate(256, fish.dup), "\n")
