course = File.readlines('../day_2.txt').map { |l| a,b = l.split; [a, b.to_i] }

x, depth, aim = 0, 0, 0
course.each do |cmd, n|
  case cmd
  when "forward" then x += n; depth += aim * n
  when "up"      then aim -= n
  when "down"    then aim += n
  end
end
print("part 1: ", x*aim, "\n")
print("part 2: ", x*depth, "\n")
