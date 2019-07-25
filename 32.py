'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

'''


'''
Considerando que solo números de tres cifras multiplicados por números de dos cifras generan numeros de 4 cifras restantes y que, por otra parte,
numeros de cuatro cifras multiplicados por numeros de una cifra también generan las cuatro cifras restantes, solo me base en hacer fuerza bruta en
estas cantidades de digitos para permutar.
'''

import itertools, datetime


def iterations(first_ndigits, second_ndigits):
    digits = [1,2,3,4,5,6,7,8,9]
    products = set(())
    for item in itertools.permutations(digits, first_ndigits):
            rest = digits.copy()
            rest = [n for n in rest if n not in item]
            mul_1 = int(''.join(str(i) for i in item))
            for sub_item in itertools.permutations(rest, second_ndigits):
                mul_2 = int(''.join(str(i) for i in sub_item))
                sub_rest = digits.copy()
                sub_rest = set([s for s in digits if s not in item and s not in sub_item])
                mul_2 = int(''.join(str(i) for i in sub_item))
                prod = mul_1 * mul_2
                if len(str(prod)) == 4:
                    set_prod = set([int(n) for n in str(prod)])
                    if set_prod == sub_rest:
                        products.add(prod)
    return products

def p32():
    products = iterations(4,1)
    products.update(iterations(3,2))
    return sum(products)
tt1 = datetime.datetime.now()
print('Answer: ',p32())
tt2 = datetime.datetime.now()
print('Performance: ',(tt2-tt1))

