P1 = 1; P2 = 10

d100 = (1..100).cycle
n_rolls = 0
pos = [P1-1, P2-1]
scores = [0, 0]
player = 0
until scores.max >= 1000
  n_rolls += 3
  pos[player] = (pos[player] + d100.next + d100.next + d100.next) % 10
  scores[player] += pos[player] + 1
  player = 1 - player
end
puts "part 1: #{scores.min * n_rolls}"

# universe count per rolls sum
dirac_outcomes = [1,2,3].repeated_permutation(3).group_by(&:sum).transform_values(&:size)
universes = { [[P1-1, 0], [P2-1, 0]] => 1 }
wins = [0, 0]
player = 0
while universes.size > 0 do
  n_universes = Hash.new(0)
  universes.each_pair do |u, count|
    pos, score = u[player]
    dirac_outcomes.each do |roll, freq|
      n_pos = (pos + roll) % 10
      n_score = score + n_pos + 1
      if n_score >= 21
        wins[player] += count * freq
      else
        n_u = u.dup
        n_u[player] = [n_pos, n_score]
        n_universes[n_u] += count * freq
      end
    end
  end
  player = 1 - player
  universes = n_universes
end
puts "part 2: #{wins.max}"

