import math, itertools, datetime
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

def is_prime_proof(n):
    toCheck = []
    toCheck.append(int(n[:-1]+'1'))
    toCheck.append(int(n[:-1]+'3'))
    toCheck.append(int(n[:-1]+'7'))
    toCheck.append(int(n[:-1]+'9'))
    isPrime = False
    for num in toCheck:
        if num < 3 or num % 2 == 0:
            isPrime = (num == 2)
        else:
            isPrime = all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))
        if isPrime: break
    return not isPrime

def p200():
    """ Problem 200 """
    limit = 1000000
    primes = prime_sieve(limit)
    i, i2, i3,i4, i5 = 1, 1, 1, 3, 3
    print(primes[:5])
    sqube = None
    sqube2 = primes[i2]**2 * 8
    sqube3 = primes[i3]**3 * 4
    sqube4 = primes[i4]**2 * 125
    sqube5 = primes[i5]**3 * 25
    while i <= 200:
        sqube = min(sqube2, sqube3, sqube4,sqube5)
        ssqube = str(sqube)
        if '200' in ssqube:
            if (is_prime_proof(ssqube)):
                i += 1
        if sqube is sqube2:
            i2 += 1
            sqube2 = primes[i2]**2 * 8
        elif sqube is sqube3:
            i3 += 1
            sqube3 = primes[i3]**3 * 4
        elif sqube is sqube4:
            i4 += 1
            sqube4 = primes[i4]**2 * 125
        else:
            i5+=1
            sqube5 = primes[i5]**3 * 25
    return sqube




tt1 =datetime.datetime.now()
print(p200())

print('Execute time:{} seconds'.format(datetime.datetime.now()-tt1))

