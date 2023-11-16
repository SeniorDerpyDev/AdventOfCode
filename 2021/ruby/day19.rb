require 'set'

Rotations = [[-1, -1, -1, :x, :z, :y], [-1, -1, -1, :y, :x, :z], [-1, -1, -1, :z, :y, :x],
  [-1, -1, 1, :x, :y, :z], [-1, -1, 1, :y, :z, :x], [-1, -1, 1, :z, :x, :y],
  [-1, 1, -1, :x, :y, :z], [-1, 1, -1, :y, :z, :x], [-1, 1, -1, :z, :x, :y],
  [-1, 1, 1, :x, :z, :y], [-1, 1, 1, :y, :x, :z], [-1, 1, 1, :z, :y, :x],
  [1, -1, -1, :x, :y, :z], [1, -1, -1, :y, :z, :x], [1, -1, -1, :z, :x, :y],
  [1, -1, 1, :x, :z, :y], [1, -1, 1, :y, :x, :z], [1, -1, 1, :z, :y, :x],
  [1, 1, -1, :x, :z, :y], [1, 1, -1, :y, :x, :z], [1, 1, -1, :z, :y, :x],
  [1, 1, 1, :x, :y, :z], [1, 1, 1, :y, :z, :x], [1, 1, 1, :z, :x, :y]]

Point = Struct.new(:x, :y, :z) do
  def +(other)
    Point.new(x + other.x, y + other.y, z + other.z)
  end
  def -(other)
    Point.new(x - other.x, y - other.y, z - other.z)
  end
  def manhattan_dist(other)
    (x - other.x).abs + (y - other.y).abs + (z - other.z).abs
  end
  def rotate(r)
    sx, sy, sz, vx, vy, vz = r
    Point.new(sx * self[vx], sy * self[vy], sz * self[vz])
  end
end

def align(s, s0)
  Rotations.each do |r|
    vectors = Hash.new(0)
    rotated = s[:beacons].map { |p| p.rotate(r) }
    rotated.each do |b|
      s0[:beacons].each do |b0|
        vectors[b0 - b] += 1
      end
    end
    best = vectors.values.max
    if best >= 12
      vec, _ = vectors.find { |k, v| v == best }
      s[:pos] = s0[:pos] + vec
      s[:beacons] = rotated
      return s
    end
  end
  nil
end

scanners = File.read('../day_19.txt').split("\n\n").map do |s|
  { :beacons => s.lines.drop(1).map { |line| Point.new *(line.chomp.split(',').map &:to_i) } }
end

s0 = scanners.shift
s0[:pos] = Point.new(0, 0, 0)
aligned_scanners = [s0]
all_the_beacons = Set[*s0[:beacons]]
while scanners.size > 0
  s = scanners.shift
  aligned = nil
  aligned_scanners.each do |ref|
    aligned = align(s, ref)
    break if aligned
  end
  if aligned
    aligned_scanners << aligned
    aligned[:beacons].each { |b| all_the_beacons << aligned[:pos] + b }
  else
    scanners << s
  end
end

puts "part 1: #{all_the_beacons.size}"
max_dist = aligned_scanners.combination(2).map { |s0, s1| s0[:pos].manhattan_dist(s1[:pos]) }.max
puts "part 2: #{max_dist}"
