import std/strscans, std/seqUtils

type Cuboid = array[6, int]

type Instruction = object
    c: Cuboid
    s: bool

func difference(c1: Cuboid, c2: Cuboid): seq[Cuboid] =
    var overlap: Cuboid
    for i in [0, 2, 4]:
        if c1[i] <= c2[i+1] and c2[i] <= c1[i+1]:
            overlap[i] = max(c1[i], c2[i])
            overlap[i+1] = min(c1[i+1], c2[i+1])
        else:
            return @[c1]

    if c1[0] != overlap[0]:
        result.add [c1[0], overlap[0]-1, c1[2], c1[3], c1[4], c1[5]]
    if c1[1] != overlap[1]:
        result.add [overlap[1]+1, c1[1], c1[2], c1[3], c1[4], c1[5]]
    if c1[2] != overlap[2]:
        result.add [overlap[0], overlap[1], c1[2], overlap[2]-1, c1[4], c1[5]]
    if c1[3] != overlap[3]:
        result.add [overlap[0], overlap[1], overlap[3]+1, c1[3], c1[4], c1[5]]
    if c1[4] != overlap[4]:
        result.add [overlap[0], overlap[1], overlap[2], overlap[3], c1[4], overlap[4]-1]
    if c1[5] != overlap[5]:
        result.add [overlap[0], overlap[1], overlap[2], overlap[3], overlap[5]+1, c1[5]]

proc parse(l: string): Instruction =
    let (ok, status, x0, x1, y0, y1, z0, z1) = l.scanTuple("$* x=$i..$i,y=$i..$i,z=$i..$i")
    result.c = [x0, x1, y0, y1, z0, z1]
    result.s = status == "on"

let instructions = "../day_22.txt".lines.toSeq.map(parse)

var cuboids: seq[Cuboid]
for i in instructions:
    var new_cuboids = if i.s: @[i.c] else: @[]
    for c in cuboids:
        new_cuboids &= c.difference(i.c)
    cuboids = new_cuboids

var t1, t2: int64
for c in cuboids:
    let vol = (c[1]-c[0]+1) * (c[3]-c[2]+1) * (c[5]-c[4]+1)
    if c[0] <= 50 and c[0] >= -50:
        t1 += vol
    t2 += vol
echo "part 1: ", t1
echo "part 2: ", t2
