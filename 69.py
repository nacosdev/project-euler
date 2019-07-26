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

primes = prime_sieve(100)

def divisors_of(n):
    return [x for x in range(1, int(math.sqrt(n)) * 2, 1) if n % x == 0 and is_prime(x)]


def relative_primes(n):
    divisors = divisors_of(n)
    print(n, divisors)
    relatives = []
    relatives = [x for x in range(1,n,2)]
    for item in divisors: 
        [relatives.remove(x) for x in relatives if x % item == 0]
    return relatives

tt1 = datetime.datetime.now()
maxi = 0 
nmax = 0
for x in range (4,500, 2):
    phi = len(relative_primes(x))
    tam = x / phi
    if tam > maxi:
        nmax = x
        maxi = tam
print(maxi, nmax)
tt2 = datetime.datetime.now()
print('Tardo: ', tt2-tt1)


# 10000 en 36 segundos, 4.8125 2310