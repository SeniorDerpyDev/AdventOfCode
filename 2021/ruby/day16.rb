Packet = Struct.new(:version, :type, :value, :packets) do
  def sum_versions
    version + packets.sum(&:sum_versions)
  end

  def eval
    case type
    when 0 then packets.sum(&:eval)
    when 1 then packets.map(&:eval).reduce(:*)
    when 2 then packets.map(&:eval).min
    when 3 then packets.map(&:eval).max
    when 4 then value
    when 5 then packets[0].eval > packets[1].eval ? 1 : 0
    when 6 then packets[0].eval < packets[1].eval ? 1 : 0
    when 7 then packets[0].eval == packets[1].eval ? 1 : 0
    end
  end
end

def parse_packet(s, i = 0)
  version = s[i..i+2].to_i(2)
  type = s[i+3..i+5].to_i(2)
  value = nil
  packets = []
  i += 6
  if type == 4
    x = ""
    while s[i] == "1"
      x += s[i+1..i+4]
      i += 5
    end
    x += s[i+1..i+4]
    value = x.to_i(2)
    i += 5
  else
    if s[i] == "0"
      i += 1
      j = i + 15 + s[i..i+14].to_i(2)
      i += 15
      while i < j
        pkt, i = parse_packet(s, i)
        packets << pkt
      end
    else
      i += 1
      n = s[i..i+10].to_i(2)
      i += 11
      n.times do
        pkt, i = parse_packet(s, i)
        packets << pkt
      end
    end
  end
  return [Packet.new(version, type, value, packets), i]
end

bits = File.read("../day_16.txt").chomp.chars.map { |c| '%04b' % c.hex }.join
pkt, _ = parse_packet(bits)
puts "part 1: #{pkt.sum_versions}"
puts "part 2: #{pkt.eval}"
