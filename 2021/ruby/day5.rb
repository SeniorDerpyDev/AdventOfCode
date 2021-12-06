vent_lines = File.readlines("../day_5.txt").map do |l|
  l.split(" -> ").map{ |p| p.split(",").map &:to_i }
end

def run(lines, part)
  lines.each_with_object(Hash.new(0)) do |((x1, y1), (x2, y2)), points|
    next if part == 1 && x1 != x2 && y1 != y2
    dx, dy = x2 <=> x1, y2 <=> y1
    (1+[(x2-x1).abs, (y2-y1).abs].max).times do |n|
      points[[x1 + n*dx, y1 + n*dy]] += 1
    end
  end.count { |k,v| v>1 }
end

print("part 1: ", run(vent_lines, 1), "\n")
print("part 2: ", run(vent_lines, 2), "\n")
