'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
import math, itertools,datetime

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))


def p41():# el máximo debe tener las cifras de 1 a 7, ya si le agrego 8 o 9, la suma de sus cifras es multiplo de 3
    ns = [2,4,5,6]# Como cualquier numero primo termina en 1, 7, 3 ,9 separo las cifras para que no haga permutaciones de más
    ls = [1,3,7]
    maxi = 0
    for l in ls:
        r_l = ls.copy()
        r_l.remove(l)
        for item in itertools.permutations(ns + r_l):
            list_n = list(item) + [l]
            n = int(''.join([str(x) for x in list_n]))
            if is_prime(n):
                if n > maxi:
                    maxi = n
    return n


tt1 = datetime.datetime.now()
print('Max:', p41()) # 3165427
tt2 = datetime.datetime.now()
print('Execute time:', tt2 - tt1) # 0.1 seconds
