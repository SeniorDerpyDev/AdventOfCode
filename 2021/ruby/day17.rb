t_x = 117..164; t_y = -140..-89

vx_min, vx_max = ((Math.sqrt(1+8*t_x.min) - 1) / 2).ceil, t_x.max
vy_min, vy_max = t_y.min, -t_y.min - 1

puts "part 1: #{vy_max * (vy_max + 1) / 2}"

solutions = 0
(vx_min..vx_max).each do |i_vx|
  (vy_min..vy_max).each do |i_vy|
    x, y, vx, vy = 0, 0, i_vx, i_vy
    until x > t_x.max || y < t_y.min
      x += vx; y += vy
      vx -= 1 if vx > 0
      vy -= 1
      if t_x.include?(x) && t_y.include?(y)
        solutions += 1
        break
      end
    end
  end
end
puts "part 2: #{solutions}"
