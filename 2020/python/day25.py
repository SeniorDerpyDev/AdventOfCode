door_pub_key = 14012298
card_pub_key = 74241

loop, n = 0, 1
while n != door_pub_key:
    n = n*7 % 20201227
    loop += 1

print('part 1:', pow(card_pub_key, loop, 20201227))

