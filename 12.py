from collections import defaultdict
import math, datetime
'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''



def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

def number_of_divisors_optimized(n):
    """
    based on
    https://www.math.upenn.edu/~deturck/m170/wk2/numdivisors.html
    """
    dict_divisors = defaultdict(int)
    divisors = 1
    resto = n
    while True:
        if is_prime(resto):
            dict_divisors[resto] += 1
            break
        for x in range(2, int(math.sqrt(resto)+ 1)):
            if resto % x is 0:
                dict_divisors[x] += 1
                resto = resto // x
                break
    for v in dict_divisors.values():
        divisors *= (v + 1)
    return divisors




def p12():
    triangle = 0
    vueltas = 1
    while True:
        triangle += vueltas
        vueltas += 1
        if triangle % 2 is not 0: continue
        if number_of_divisors_optimized(triangle) > 500:
            return triangle



tt1 = datetime.datetime.now()
print(p12())
tt2 = datetime.datetime.now()

print('{} seconds'.format((tt2-tt1).seconds))

