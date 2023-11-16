class Range
    def and(other)
        l1, r1 = self.min, self.max
        l2, r2 = other.min, other.max
        [l1, l2].max .. [r1, r2].min
    end

    def empty?
        size.zero?
    end
end

class Cuboid
  attr_reader :x, :y, :z

  def initialize(x, y, z)
    @x, @y, @z = x, y, z
  end

  def vol
    @x.size * @y.size * @z.size
  end

  def intersect(other)
    x = @x.and other.x
    y = @y.and other.y
    z = @z.and other.z
    Cuboid.new(x, y, z) unless x.empty? or y.empty? or z.empty?
  end
end

def run(steps)
  on, off = [], []
  steps.each do |switch, cuboid|
    n_on = off.map { |c| c.intersect cuboid }.compact
    n_off = on.map { |c| c.intersect cuboid }.compact
    on.concat(n_on)
    off.concat(n_off)
    on << cuboid if switch
  end
  on.sum(&:vol) - off.sum(&:vol)
end

steps = File.readlines('../day_22.txt', chomp: true).map do |line|
  switch, ranges = line.split
  [switch == 'on', Cuboid.new(*ranges.split(',').map { |r| eval r[2..-1] })]
end
init_steps = steps.reject { |_, c| c.x.and(-50..50).empty? or c.y.and(-50..50).empty? or c.z.and(-50..50).empty? }
puts "part 1: #{run(init_steps)}"
puts "part 2: #{run(steps)}"
