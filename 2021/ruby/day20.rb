def enhance(img, algorithm, size, steps)
  grid = [-1,0,1].product([-1,0,1])
  mn = 0; mx = size - 1
  steps.times do
    tmp = Hash.new(algorithm[0] && !img.default)
    mn -= 1; mx += 1
    mn.upto(mx) do |x|
      mn.upto(mx) do |y|
        idx = grid.reduce(0) { |n, p| dy, dx = p; n * 2 + (img[[x+dx, y+dy]] ? 1 : 0) }
        tmp[[x,y]] = algorithm[idx]
      end
    end
    img = tmp
  end
  img.count { |k,v| v }
end

a, i = File.read('../day_20.txt').split("\n\n")
algorithm = a.chars.map { |c| c == '#' }
img = Hash.new(false)
i.lines.each_with_index { |line, y| line.chomp.chars.each_with_index { |c, x| img[[x,y]] = c=='#' } }

puts "part 1: #{enhance(img, algorithm, i.lines.size, 2)}"
puts "part 2: #{enhance(img, algorithm, i.lines.size, 50)}"
