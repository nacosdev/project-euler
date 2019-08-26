'''

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits
in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

'''
import datetime


def p57():
    """
    La relacion entre tanto un denominador como numerador, con el siguente, es siempre de 2 * n[i] + n[i - 1] donde n se entiende como numerador o denominador
    e i hace referencia a la posicion de estos.
    """
    last_denominator = 2
    last_numerator = 3
    denominator = 5
    numerator = 7
    number = 0
    for x in range(1, 1001):
        new_numerator = (numerator * 2) + last_numerator
        new_denominator = (denominator * 2) + last_denominator

        if len(str(new_numerator)) > len(str(new_denominator)):
            number += 1
        last_numerator = numerator
        last_denominator = denominator

        denominator = new_denominator
        numerator = new_numerator
    return number

tt1 = datetime.datetime.now()

print('Answer: ', p57()) #153

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.01 seconds