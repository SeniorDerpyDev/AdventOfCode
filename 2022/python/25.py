t = 0
for l in open(0):
    n = 0
    for c in l.strip():
        n *= 5
        n += "=-012".index(c) - 2
    t += n

snafu = ""
while t:
    d = t % 5
    t //= 5
    if d > 2: t += 1
    snafu = "012=-"[d] + snafu
print(snafu)

