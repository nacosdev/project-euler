import math, itertools
'''
We shall define a sqube to be a number of the form, p^2 q^3, where p and q are distinct primes.
For example, 200 = 5^2 2^3 or 120072949 = 23^2 61^3.

The first five squbes are 72, 108, 200, 392, and 500.

Interestingly, 200 is also the first number for which you cannot change any single digit to make a prime; we shall call such numbers, prime-proof.
The next prime-proof sqube which contains the contiguous sub-string "200" is 1992008.

Find the 200th prime-proof sqube containing the contiguous sub-string "200".
'''
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

#def is_prime_proof()

def p200():
    """ Problem 200 """
    limit = 100_000
    primes = prime_sieve(limit)
    i, i2, i3 = 1, 1, 1
    sqube2 = primes[i2]**2 * 8
    sqube3 = primes[i3]**3 * 4
    while i <= 10:
        sqube = min(sqube2, sqube3)
        if '200' in str(sqube):
            print(i, sqube)
            i += 1
        if sqube2 < sqube3:
            i2 += 1
            sqube2 = primes[i2]**2 * 8
        else:
            i3 += 1
            sqube3 = primes[i3]**3 * 4

#p200()
#lista = [x for x in range(0,50)]

for item in itertools.permutations([1,2,3,4,5,6,7,8]):
    print(item)




