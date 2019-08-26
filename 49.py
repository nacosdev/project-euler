'''

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are
prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''
import math, itertools, datetime

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

#def find_arithmetic(deph):


def p49():
    sumando = 3330
    primes = [x for x in prime_sieve(6800) if x > 999]
    finded = 0
    for first in primes:
        second = first + sumando
        if is_prime(second) and sorted(str(first)) == sorted(str(second)):
            third = second + sumando
            if is_prime(third) and sorted(str(second)) == sorted(str(third)):
                finded += 1
                if finded == 2:
                    return str(first) + str(second) + str(third)

tt1 = datetime.datetime.now()

print('Answer: ',p49()) # 296962999629

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) #0.001 second