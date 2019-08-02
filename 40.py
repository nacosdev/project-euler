

import datetime


def create_irrational(maxi, positions):
    numbers  = []
    n = 1
    position = 10
    ns = []
    while position < maxi:
        for x in range(0, 10):
            for i in str(n):
                if position in positions:
                    numbers.append(i)
                position += 1
            if position in positions:
                numbers.append(x)
            position += 1
        n += 1
    return numbers

def p40():
    numbers = create_irrational(1000001, [1,10,100,1000,10000,100000,1000000])
    total = 1
    for n in numbers:
        total *= int(n)
    return total


tt1 = datetime.datetime.now()
print('Answer: ', p40())
tt2 = datetime.datetime.now()
print('Execute time: ', tt2 - tt1) # 0.2 seconds
