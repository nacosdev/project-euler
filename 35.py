'''

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

'''
import numpy as np
import math, itertools, datetime

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

def prime_sieve_only_circulars(n):
    primes = np.ones(n, dtype=bool)
    primes[0] = primes[1] = False
    for x in range(2, int(math.sqrt(n)) + 1):
        if primes[x]:
            primes[x*x::x] = False
    return [x for x,v in enumerate(primes) if v and all(x in ['3', '7','9','1'] for x in str(x))]

def is_circular(n):
    is_circular_prime = True
    for x in range(len(n)):
        new_str = n[x:] + n[:x]
        if not is_prime(int(new_str)):
            return False
    return is_circular_prime


def p35(maxi = 1000000):
    count = 0
    posible_circular = [2, 5] + prime_sieve_only_circulars(maxi) 
    for p in posible_circular:
        if is_circular(str(p)):
            count += 1
    return count

tt1 = datetime.datetime.now()

print('Answer: ', p35()) # 55

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.2 seconds