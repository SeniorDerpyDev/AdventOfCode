octos = File.readlines('../day_11.txt', chomp: true).map { |l| l.chars.map &:to_i }
dirs = [-1,0,1].product([-1,0,1]) - [[0,0]]

step, flash_count = 0, 0
while octos.any? { |r| r != [0]*10 }
  flashes, flashed = [], []
  10.times { |y| 10.times { |x| flashes << [y, x] if 10 == octos[y][x] += 1 } }
  while flashes.size > 0
    y, x = flashes.shift
    flashed << [y, x]
    flash_count += 1
    dirs.map { |dy,dx| [y+dy, x+dx] }
      .select { |y,x| (0...10).include?(y) && (0...10).include?(x) }
      .each { |ny, nx| flashes << [ny, nx] if 10 == octos[ny][nx] += 1 }
  end
  flashed.each { |y,x| octos[y][x] = 0 }
  step +=1
  puts "part 1 : #{flash_count}" if step == 100
end
puts "part 2 : #{step}"
