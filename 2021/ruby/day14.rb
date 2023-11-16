input = File.readlines('../day_14.txt', chomp: true)
polymer = input[0]
$rules = input.drop(2).each_with_object(Hash.new) do |line, h|
  pair, elem = line.split(" -> ")
  h[pair] = elem
end

def run(polymer, n_steps)
  elements = polymer.chars.each_with_object(Hash.new(0)) { |c, h| h[c] += 1 }
  pairs = polymer.chars.each_cons(2).with_object(Hash.new(0)) { |p, h| h[p.join] += 1 }
  n_steps.times do
    pairs.select { |pair, n| n > 0 }.each do |pair, n|
      l, m, r = pair[0], $rules[pair], pair[1]
      pairs[pair] -= n
      pairs[l+m] += n
      pairs[m+r] += n
      elements[m] += n
    end
  end
  min, max = elements.values.minmax
  max - min
end

puts "part 1: #{run(polymer, 10)}"
puts "part 2: #{run(polymer, 40)}"
