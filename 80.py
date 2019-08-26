'''

It is well known that if the square root of a natural number is not an integer, then it is irrational. The decimal expansion of such square roots is infinite
without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

'''
from decimal import Decimal, localcontext
import math, datetime




def p80():
    suma = 0
    sumandos = 0
    x = 0
    with localcontext() as ctx: #
        ctx.prec = 105
        Decimal(2).sqrt()
        for x in range(1, 100):
            number = Decimal(x).sqrt()
            str_dec = str(number).replace('.','')
            if len(str_dec) > 99:
                suma += sum([int(x) for x in str_dec[:100]])

    return suma

tt1 = datetime.datetime.now()

print('Answer: ', p80()) # 40886

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.005 seconds