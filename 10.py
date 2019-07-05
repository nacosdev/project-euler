import math#The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#Find the sum of all the primes below two million.
def sum_primes_below(n):
    lista = [x for x in range(3, n, 2) if x % 3 is not 0 and x % 5 is not 0 and x % 7 is not 0]
    index = 0
    primes = [2,3,5,7]
    suma = sum(primes)
    last = 13
    while last <=  math.sqrt(n)+1:
        for item in lista:
            if item % last == 0:
                lista.remove(item)
        last = lista[0]
        suma += last
    return suma + sum(lista[1:])


print(sum_primes_below(2000000))
