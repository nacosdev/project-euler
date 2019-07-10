import math
import functools
import operator

'''
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''
#k = 7: 12 [1,1,1,1,4,3,1]
#k = 8: 12 [1,1,1,1,3,2,1,2]
#k = 9: 15 [1,5,1,1,1,3,1,1,1]
#K = 10: 16 [1,1,4,4,1,1,1,1,1,1]
#k = 11: 16 [1,1,2,2,4,1,1,1,1,1,1]
#k = 12: 16 [1,1,1,1,2,1,2,1,2,1,2,1]
#Nums = [1,1,1,1,2,1,2,1,2,1,2,1]
#suma = 0
#prod = 1

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))


#primero pruebo poniendo todos los dos, hasta que el producto sea mayor a la suma, para saber cuantas posiciones voy a usar como maximo
def p88(k):
    muls = []
    equal = False
    while True:
        muls.append(2)
        Nums = [1] * (k-len(muls)) + muls
        suma = sum(Nums)
        prod = 1
        for num in muls:
            prod *= num
        if prod is suma:
            return Nums
        if prod * 2 > suma:
            break
    #muls.remove(2)
    solutions = []
    vueltas = 0
    while vueltas < 20:
        nums, suma, prod, equal = traer_resultados(k,muls)
        if prod < suma:
            muls 
        vueltas += 1


def traer_resultados(k,muls):
    """
    muls son los multiplos que se estan probando
    prueba combinaciones, y rellena los espacios restantes con unos para ver si es igual
    """
    Nums = [1] * (k-len(muls)) + muls
    suma = sum(Nums)
    prod = 1
    for num in muls:
        prod *= num
    return Nums, suma, prod, prod is suma

'''
response = p88(100)
print(response)
#Nums = [1,1,2,2,2,2,1,1,1,1]
Nums = response

suma = 0
prod = 1
for n in Nums:
    suma += n
    prod *= n
#Nums, suma, prod, igual = traer_resultados(7,[4,3])
print('Suma: {}, Producto: {}, Tamanho: {}, Es igual: '.format(suma,prod, len(Nums)))#, igual))
'''


