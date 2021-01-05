door_pub_key = 14012298
card_pub_key = 74241

def find_loop_value(n):
    i = 1
    while pow(7, i, 20201227) != n:
        i += 1
    return i

encryption_key = pow(card_pub_key, find_loop_value(door_pub_key), 20201227)
print('part 1:', encryption_key)

