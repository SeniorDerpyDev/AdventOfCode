# Determine the quality level of each blueprint by multiplying that blueprint's ID number
# with the largest number of geodes that can be opened in 24 minutes using that blueprint.
# T1: 33
# P1: 1177
#
# Determine the largest number of geodes you could open in 32 minutes using each of the first three blueprints.
# What do you get if you multiply these numbers together?
# P2: 62744
from math import ceil

BP = []
for l in open(0):
    w = l.strip().split()
    BP.append( [(int(w[6]), 0, 0, 0), (int(w[12]), 0, 0, 0), (int(w[18]), int(w[21]), 0, 0), (int(w[27]), 0, int(w[30]), 0)] )

M_COST = [tuple(max(*t) for t in zip(*bp)) for bp in BP]
M_COST = [t[:-1] + (1000,) for t in M_COST]

def solve(i, t, robots, mats):
    if t <= 0:
        return mats[3]

    key = (t, ) + robots + mats
    if key in CACHE:
        return CACHE[key]

    bp = BP[i]
    mc = M_COST[i]

    best = mats[3] + robots[3] * t
    for ri in range(4):
        if robots[ri] > 0:
            d = max( ceil((bp[ri][n] - mats[n]) / robots[n]) for n in range(4) if robots[n] > 0 and bp[ri][n] > 0)
            if 0 < d <= t:
                robots_ = robots[:ri] + (1+robots[ri],) + robots[ri+1:]
                mats_ = tuple(min(mc[n]*2, mats[n] - bp[ri][n] + d*robots[n]) for n in range(4))
                best = max(best, solve(i, t-d, robots_, mats_))
    for ri in range(4):
        if robots[ri] < mc[ri] and all(mats[n] >= bp[ri][n] for n in range(4)):
            robots_ = robots[:ri] + (1+robots[ri],) + robots[ri+1:]
            mats_ = tuple(min(mc[n]*2, mats[n] - bp[ri][n] + robots[n]) for n in range(4))
            best = max(best, solve(i, t-1, robots_, mats_))
    CACHE[key] = best
    return best

p1 = 0
for i in range(len(BP)):
    CACHE = {}
    p1 += (i + 1) * solve(i, 24, (1, 0, 0, 0), (0, 0, 0, 0))
print(p1)

# p2 = 1
# for i in range(3):
#     CACHE = {}
#     p2 *= solve(i, 32, (1, 0, 0, 0), (0, 0, 0, 0))
# print(p1)

