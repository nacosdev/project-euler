'''


Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


'''
import datetime
def is_pandigitable(n):
    str_n = str(n)
    multiplier = 2
    while True:
        str_n += str(n * multiplier)
        if len(str_n) == 9:
            if ''.join(sorted(str_n)) == '123456789':
                return int(str_n)
            return False
        if len(str_n) > 9:
            return False
        multiplier += 1


def p38():
    maxi = is_pandigitable(9)
    start = int(str(maxi)[:2])
    for x in range(start, 100):
        pandigital = is_pandigitable(x)
        if pandigital > maxi:
            maxi = pandigital
    start = int(str(maxi)[:3])
    for x in range(start, 1000):
        pandigital = is_pandigitable(x)
        if pandigital > maxi:
            maxi = pandigital

    start = int(str(maxi)[:4])
    for x in range(start, 10000):
        pandigital = is_pandigitable(x)
        if pandigital > maxi:
            maxi = pandigital
    return maxi

tt1 = datetime.datetime.now()

print('Answer: ',p38())

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.001 seconds


