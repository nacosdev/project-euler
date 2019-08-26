from collections import defaultdict
import math, datetime

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

def factorize(n):
    dict_fact = defaultdict(int)
    div = 2
    if is_prime(n):
        dict_fact[n] += 1
        return dict_fact
    while True:
        if n % div == 0:
            dict_fact[div] += 1
            n = n // div
            if is_prime(n):
                dict_fact[n] += 1
                return dict_fact
            div = 2
        else:
            div += 1

def p69(maximo):
    maxi = 0
    max_n = None
    for n in range(10, maximo,10):
        response = factorize(n)
        result = n
        for k in response:
            result *= (1 - (1 / k))
        partial = (n / result)
        if partial > maxi:
            max_n = n
            maxi = partial

    return max_n
tt1 = datetime.datetime.now()

print('Answer: ', p69(1000000)) # 510510

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 1.5 seconds

