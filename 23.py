'''


A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper
limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
import math, datetime
def d(n):
    inc = 1
    start = 2
    if n % 2 != 0:
        start = 3
        inc = 2
    nums = set(())
    for x in range(start, int(math.sqrt(n) + 1), inc):
        if (n % x) == 0:
            nums.add(x)
            nums.add(n // x)
    return sum(nums) + 1


def p23(maxi):
    even_abundants = []
    odd_abundants = []
    for x in range(1,maxi):
        if d(x) > x:
            if x % 2 == 0:
                even_abundants.append(x)
            else:
                odd_abundants.append(x)
    suma = 0
    for x in range(1, maxi):
        if x % 2 == 0:
            for n in even_abundants:
                if (x - n) < 0:
                    suma += x
                    break
                elif (x - n) in even_abundants:
                    break
        else:
             for n in odd_abundants:
                if (x - n) < 0:
                    suma += x
                    break
                elif (x - n) in even_abundants:
                    break
    return suma
    #for n in even_abundants:
        #print(n)

tt1 = datetime.datetime.now()

print(p23(28123))

tt2 = datetime.datetime.now()

print('Execute time ', tt2 - tt1) #6 seconds