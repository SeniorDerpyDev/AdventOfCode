def parse(s)
  number = []
  depth = 0
  s.chars.each do |c|
    case c
    when '[' then depth += 1
    when ']' then depth -= 1
    when ',' then next
    else number << [c.to_i, depth]
    end
  end
  number
end

def explode(number)
  i = number.index { |_,d| d > 4 }
  return false unless i
  l, r = i, i + 1
  number[l-1][0] += number[l][0] if l > 0
  number[r+1][0] += number[r][0] if r+1 < number.size
  number[i][0] = 0
  number[i][1] -= 1
  number.delete_at(i+1)
  return true
end

def split(number)
  i = number.index { |n,_| n > 9 }
  return false unless i
  n, d = number[i]
  l, r = n/2, n - (n/2)
  number[i][0] = l
  number[i][1] = d+1
  number.insert(i+1, [r, d+1])
end

def reduce(number)
  loop do
    next if explode(number)
    break unless split(number)
  end
  number
end

def magnitude(number)
  result = 0
  depth = number.map { |_,d| d }.max
  while number.size > 1
    while (i = number.index { |_,d| d == depth })
      number[i][0] = number[i][0]*3 + number[i+1][0]*2
      number[i][1] -= 1
      number.delete_at(i+1)
    end
    depth -= 1
  end
  number[0][0]
end

def add(n1, n2)
  reduce(n1.map { |m, d| [m, d + 1] } + n2.map { |m, d| [m, d + 1] })
end

numbers = File.readlines("../day_18.txt", chomp: true).map { |l| parse(l) }
puts "part 1: #{magnitude(numbers.inject { |l,r| add(l, r) })}"

max_magnitude = numbers.permutation(2).map { |n1, n2| magnitude(add(n1, n2)) }.max
puts "part 2: #{max_magnitude}"

