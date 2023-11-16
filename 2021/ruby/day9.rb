hmap = File.readlines("../day_9.txt", chomp: true).map { |l| [9] + l.chars.map(&:to_i) + [9] }
len = hmap[0].length
hmap.unshift(Array.new(len, 9))
hmap.push(Array.new(len, 9))

nbors = [[-1, 0], [1, 0], [0, -1], [0, 1]]
basins = Hash.new(0)
(1..len-2).each do |yy|
  (1..len-2).each do |xx|
    next if hmap[yy][xx] == 9
    y, x = yy, xx
    while true
      nbor = nbors.map { |dy,dx| [y+dy, x+dx] }.find { |ny,nx| hmap[ny][nx] < hmap[y][x] }
      break unless nbor
      y, x = nbor
    end
    basins[[y, x]] += 1
  end
end

print("part 1: ", basins.keys.sum { |y,x| hmap[y][x] + 1 }, "\n")
print("part 2: ", basins.values.max(3).reduce(1, :*), "\n")
