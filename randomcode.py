import random


def random_str(l):
    skey = ''
    for i in range(l):
        skey += (random.choice('0123456789abcde'))

    return skey

print(random_str(32))