def prime_factors(n):
    primes_factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primes_factors.append(i)
    primes_factors.append(n)
    return primes_factors
print(prime_factors(600851475143)[-1])
