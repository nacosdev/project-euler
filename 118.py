import math, json
import itertools
'''
Using all of the digits 1 through 9 and concatenating them freely to form decimal integers, different sets
can be formed. Interestingly with the set {2,5,47,89,631}, all of the elements belonging to it are prime.

How many distinct sets containing each of the digits one through nine exactly once contain only prime elements?
'''
#La lista puede tener como máximo 5 elementos, ya que puede luego de los elementos de una cifra, el numero debee terminar en 1,3,7,9

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))



lista_grande = []
def find_set(setn,last,numbers,resto, setdistinct):
    for n in last:
        #print('ene',n)
        permutate = resto
        permutate.remove(n)
        for d in range(0, 9 - len(numbers)):
            iterable = permutate
            vueltas = d
            if d is 0:
                iterable = [2,3,5,7]
                [iterable.remove(n) for n in numbers if n in iterable]
                vueltas = 1
                if len(iterable) is 0:
                    continue
            for item in itertools.permutations(iterable,vueltas):
                if d > 0:
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
                    numbers = [n for subs in newset for n in subs]
                    rest = [n for n in range(1,10) if n not in numbers]
                    ultimos = [1,3,7,9]
                    [ultimos.remove(n) for n in numbers if n in ultimos]
                    if len(rest) is 0:
                        if set(newdisctint) not in lista_grande:
                            lista_grande.append(set(newdisctint))

                        break
                    if len(ultimos) is 0:
                        break
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
        for digits in range(1,8):
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



p118()
for item in lista_grande:
    print(item)
print('Cantidad: {}'.format(len(lista_grande)))



'''
seteado = [{1,2,3},{3,4,5}]
print(seteado)
seti = {4,5,6}
print('seti',seti)
seti.add(2)
print('seti2',seti)
print({3,2,1,3,4} in seteado)
#print(p118())17391
'''