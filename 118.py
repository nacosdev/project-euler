import math, json
import itertools
'''
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets
can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
'''


def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))


def p118():
    numbers = [2,4,5,6,8]
    last_numbers = [1,3,7,9]
    combinations = {}
    for item in last_numbers:
        lista = (numbers + last_numbers)
        lista.remove(item)
        combinations[str(item)] = lista
    total  = 4 #start in 4 for 2,3,5,7
    for key in combinations:
        for digits in range(1,4):
            #print(digits)
            for ns in itertools.permutations(combinations[key],digits):
                ns = list(ns) + [int(key)]
                if sum(ns) % 3 is 0:
                    continue
                num = int(''.join(str(n) for n in ns))
                if is_prime(num):
                    print(num)
                    total += 1
            #print(total)
    return total



print(p118())
'''
cantidad = 0
numbers = [2,4,5,6,8,1,3,7,9]
for digits in range(1,8):
    for item in itertools.permutations(numbers,digits):
        if sum(item) % 3 is 0:
            continue
        num = int(''.join(str(n) for n in item))
        if is_prime(num):
            cantidad += 1
print(cantidad)'''

'''
numbers = [2,4,5,6,8,1,3,7,9]
total = 0
for item in itertools.permutations(numbers, 9):
    print(item)
    total += 1
    if total is 30:
        break'''
