import math, json
import itertools, datetime
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

big_list = []
def find_set(setn,last,numbers,resto, setdistinct):
    for n in last:
        permutate = resto.copy()
        permutate.remove(n)
        for d in range(0, len(resto)):
            iterable = permutate.copy()
            vueltas = d
            if d is 0:
                iterable = [2,3,5,7]
                [iterable.remove(x) for x in numbers if x in iterable]
                vueltas = 1
                if len(iterable) is 0:
                    continue
            for item in itertools.permutations(iterable,vueltas):
                if d > 0:
                    if d is 8:
                        ns = list(item)
                    else:
                        ns = list(item) + [n]
                else:
                    ns = list(item)
                if sum(ns) % 3 is 0:
                    continue
                num = int(''.join(str(n) for n in ns))
                if is_prime(num):
                    newset = setn + [ns]
                    newdisctint = setdistinct + [num]
                    #set
                    numbers = [l for subs in newset for l in subs]
                    rest = [a for a in range(1,10) if a not in numbers]
                    ultimos = [1,3,7,9]
                    [ultimos.remove(s) for s in numbers if s in ultimos]
                    if len(rest) is 0:
                        #distintos
                        if set(newdisctint) not in big_list:
                            big_list.append(set(newdisctint))
                        continue
                    if len(ultimos) is 0:
                        continue
                    find_set(newset,ultimos,numbers,rest,newdisctint)

def p118():
    one_digit_primes = [2,3,5,7]
    for n in one_digit_primes:
        newset = [[n]]
        rest = [num for num in range(1,10) if num is not n]
        ultimos = [1,3,7,9]
        if n in ultimos:
            ultimos.remove(n)
        find_set(newset,ultimos,[n],rest, [n])
    numbers = [2,4,5,6,8]
    last_numbers = [1,3,7,9]
    combinations = {}
    for item in last_numbers:
        lista = (numbers + last_numbers)
        lista.remove(item)
        combinations[str(item)] = lista
    total = 0 #start in 4 for 2,3,5,7

    for key in combinations:
        for digits in range(1,5):
            for ns in itertools.permutations(combinations[key],digits):
                ns = list(ns) + [int(key)]
                if sum(ns) % 3 is 0:
                    continue
                num = int(''.join(str(n) for n in ns))
                if is_prime(num):
                    ultimos = [1,3,7,9]
                    [ultimos.remove(n) for n in ns if n in ultimos]
                    resto = [n for n in range(1,10) if n not in ns]
                    find_set([ns], ultimos, ns, resto, [num])
    return total



tt1 = datetime.datetime.now()


p118()
print('Cantidad: ', len(big_list))
print('Tardo {} segundos.'.format((datetime.datetime.now() - tt1 ).seconds)) #51 seconds


