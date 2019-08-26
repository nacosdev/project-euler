'''

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

'''
import math, datetime

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

def p50(maximo):
    primes = prime_sieve(maximo // 4)
    dict_results = {}
    max_terms = 0
    max_consecutive = 0
    for i in range(0, len(primes)):
        aux = None
        maxi = 0
        suma = 0
        terms = 0
        aux_terms = None
        for prime in primes[i:]:
            suma += prime
            terms += 1
            if suma > maximo:
                break
            if is_prime(suma):
                aux_terms = terms
                maxi = suma
        if aux_terms > max_terms:
            max_terms = aux_terms
            max_consecutive = maxi

    return max_consecutive



tt1 = datetime.datetime.now()

print('Answer: ', p50(1000000)) # 997651

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 4.3 seconds

