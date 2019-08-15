'''

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

'''
import math, itertools, datetime

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

def is_truncable(n):# right for direction, True for right, False for left
    aux = n
    while len(n) > 1:
        n = n[:-1]
        if not is_prime(int(n)):
            return False
    n = aux
    while len(n) > 1:
        n = n[1:]
        if not is_prime(int(n)):
            return False
    return True



def p37_mejorado():
    last_ls = ['3','7']
    in_ls = last_ls + ['2', '5']
    midders = ['3','7','1','9']
    finded = 0
    repeater = 0
    suma = 0
    while True:
        for item in itertools.product(midders,repeat=repeater):
            for i in itertools.permutations(in_ls,1):
                for l in itertools.permutations(last_ls,1):
                    posible_truncable = ''.join(list(i)+list(item)+list(l))
                    if is_prime(int(posible_truncable)):
                        if is_truncable(posible_truncable):
                            finded += 1
                            suma += int(posible_truncable)
                            if finded == 11:
                                return suma
        repeater += 1
tt1 = datetime.datetime.now()
print('Answer: ',p37_mejorado())
tt2 = datetime.datetime.now()

print('Execute time: ',tt2 - tt1) #0.01 second

