pairs = Hash[*"()[]{}<>".chars]
error_points = { ")" => 3,   "]" => 57,  "}" => 1197, ">" => 25137 }
compl_points = { ")" => 1,   "]" => 2,   "}" => 3,    ">" => 4 }

error_score, compl_scores = 0, []
File.readlines("../day_10.txt", chomp: true).each do |line|
  stack, err = [], false
  line.chars.each do |c|
    if pairs.has_key?(c)
      stack << pairs[c]
    elsif c != stack.pop
      error_score += error_points[c]
      err = true
      break
    end
  end
  compl_scores << stack.reverse.reduce(0) { |acc, c| acc*5 + compl_points[c] } unless err
end

print("part 1: ", error_score, "\n")
print("part 2: ", compl_scores.sort[compl_scores.length / 2], "\n")
