require 'set'

dots, folds = Set.new, []
File.readlines('../day_13.txt').each do |l|
  if /(?<axis>x|y)=(?<n>\d+)/ =~ l
    folds << [axis, n.to_i]
  elsif /(?<x>\d+),(?<y>\d+)/ =~ l
    dots << [x.to_i, y.to_i]
  end
end

part1 = false
folds.each do |axis, n|
  if axis == "x"
    dots.select { |x,y| x>n }.each { |x,y| dots.delete [x,y]; dots << [2*n-x, y] }
  else
    dots.select { |x,y| y>n }.each { |x,y| dots.delete [x,y]; dots << [x, 2*n-y] }
  end
  if !part1
    puts "part 1: #{dots.size}"
    part1 = true
  end
end

w, h = 1+dots.map { |x,y| x }.max, 1+dots.map { |x,y| y }.max
screen = Array.new(h) { Array.new(w, ' ') }
dots.each { |x,y| screen[y][x] = '#' }
puts "part 2:"
screen.each { |l| puts l.join }
