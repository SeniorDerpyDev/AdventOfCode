from collections import deque

def solve(nums, iters):
    Q = deque(range(len(nums)))
    for _ in range(iters):
        for i, n in enumerate(nums):
            p = Q.index(i)
            Q.rotate(-p)
            Q.popleft()
            Q.rotate(-n)
            Q.appendleft(i)
    z = Q.index(nums.index(0))
    return sum(nums[Q[(z + x) % len(Q)]] for x in [1000, 2000, 3000])

N = list(map(int, open(0)))
print(solve(N, 1))

N = [n * 811589153 for n in N]
print(solve(N, 10))
