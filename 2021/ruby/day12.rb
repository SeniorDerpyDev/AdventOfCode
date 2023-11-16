caves = File.readlines('../day_12.txt', chomp: true)
  .each_with_object(Hash.new { |h,k| h[k] = [] }) do |l, caves|
    a, b = l.split('-')
    caves[a] << b if a != "end" && b != "start"
    caves[b] << a if b != "end" && a != "start"
  end

def count_paths(caves, path, repeated)
  c = path.last
  return 1 if c == "end"
  if repeated
    caves[c].select { |to| to=~/[A-Z]+/ || !path.include?(to) }.sum { |nc| count_paths(caves, path + [nc], true) }
  else
    caves[c].sum { |nc| count_paths(caves, path + [nc], nc=~/[a-z]+/ && path.include?(nc)) }
  end
end

puts "part 1: #{count_paths(caves, ["start"], true)}"
puts "part 2: #{count_paths(caves, ["start"], false)}"
