require 'set'

def shortest_path(h, w, &f)
  risk = Array.new(h) { Array.new(w, Float::INFINITY) }
  risk[0][0] = 0
  queue = SortedSet[[0,0,0]]
  x, y = 0, 0
  until y == h-1 && x == w-1
    r, y, x = queue.first
    queue.delete [r, y, x]
    [[-1,0], [1,0], [0,-1], [0,1]].each do |dy, dx|
        ny, nx = y + dy, x + dx
        next unless 0 <= ny && ny < h && 0 <= nx && nx < w
        nr = f.call(ny, nx) + r
        if nr < risk[ny][nx]
          risk[ny][nx] = nr
          queue << [nr, ny, nx]
        end
      end
  end
  risk[-1][-1]
end

grid = File.readlines('../day_15.txt', chomp: true).map { |l| l.chars.map &:to_i }
h, w = grid.size, grid[0].size
part1 = shortest_path(h, w) { |y,x| grid[y][x] }
puts "part 1: #{part1}"

part2 = shortest_path(5*h, 5*w) { |y,x| (grid[y%h][x%w] - 1 + y/h + x/h) % 9 + 1 }
puts "part 2: #{part2}"

