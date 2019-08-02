'''

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

'''

import itertools

ways = []

def combinations(coins, comb):
    new_comb = comb.copy()
    new_comb.append(coins[0])
    #print(new_comb, sum(new_comb))
    new_sum = sum(new_comb)
    if new_sum == 200:
        global ways
        ways.append(new_comb)
        if coins[0] != 1:
            new_iter_comb = new_comb.copy()
            new_iter_comb[-1] = coins[1]
            combinations(coins[1:], new_iter_comb)
    elif new_sum < 200:
        new_comb.append(coins[0])
        combinations(coins, new_comb)
    else:
        new_comb[-1] = coins[1]
        combinations(coins[1:], new_comb)

def p31():
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    combinations(coins,[])
p31()
for item in ways:
    print(item)



'''

200
100 100
100 50 50
100 50 25
100 50 20 5

'''