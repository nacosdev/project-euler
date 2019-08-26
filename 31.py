'''

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''


import datetime

def combinations(coins, pos, tot):
    #print(pos, tot)
    if tot == 0:
        return 1
    if tot < 0:
        return 0
    if coins[pos] == 1: # avoid iteration to sum the rest of ones
        return 1
    if (len(coins) - pos <= 0 and tot >= 1):
        return 0
    return combinations(coins, pos + 1, tot) + combinations(coins, pos, tot - coins[pos])





def p31():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    return combinations(coins, 0, 200)



tt1 = datetime.datetime.now()

print('Answer: ', p31()) # 73682

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.05 seconds