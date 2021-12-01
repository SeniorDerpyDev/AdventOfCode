sonar = IO.readlines('../day_1.txt').map &:to_i
l = sonar.length

r1 = (0...l-1).count { |i| sonar[i] < sonar[i+1] }
print("part 1: ", r1.to_s, "\n")

r2 = (0...l-3).count { |i| sonar[i] < sonar[i+3] }
print("part 2: ", r2.to_s, "\n")
