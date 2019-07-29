'''

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''
import math, itertools, datetime
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

primes = prime_sieve(1000)
#print(primes)
def p60():
    for i, p1 in enumerate(primes):
        p1 = str(p1)
        for i2, p2 in enumerate(primes[i+1:]):
            p2 = str(p2)
            for i3, p3 in enumerate(primes[i2+1:]):
                p3 = str(p3)
                if is_remarkable([p1,p2,p3]):
                    print(p1,p2,p3)

def is_remarkable(ns):
    for com in itertools.permutations(ns,2):
        n = int(''.join([i for i in com]))
        if not is_prime(n):
            return False
    return True


tt1 = datetime.datetime.now()

print(is_remarkable(['3','7','109']))
p60()
tt2 = datetime.datetime.now()

print('Least: ', tt2-tt1)