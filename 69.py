import math, datetime

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))


def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(math.sqrt(n))+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


tt1 = datetime.datetime.now()
to = 1000
primes = prime_sieve(to)
no_primes = [x for x in range(1, to, 1)]
tt2 = datetime.datetime.now()
print('Tardo: ', tt2-tt1)


# 10000 en 36 segundos, 4.8125 2310