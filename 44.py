

 #Pn=n(3n−1)/2.
import datetime
import math as m
def isPentagonal( n ):
    # Formúla para ver si un numero es pentagonal
    n = (1 + m.sqrt(24 * n + 1)) / 6

    return( (n - int (n)) == 0)
def pentagon_at_index(x):
    #Devuelve el numero pentagonal de un determinado indice
    return (x * ((3*x) - 1) // 2)
def generate_pentagons(x = 1):
    #Generador de números pentagonales
    while True:
        yield (x * ((3*x) - 1) // 2)
        x += 1
def p44():
    '''
    Se van generando números pentagonales, y apartir de estos, se revisan todos los numeros pentagonales menores a este y se chequea si tanto
    al sumarse o al restarse con dicho número, se genera otro pentagonal.
    Se entiende que el primero encontrado es el que tiene la menor valor para D.
    '''
    a = 0
    for i,p in enumerate(generate_pentagons()):
        for x in range(1, i):
            p2 = pentagon_at_index(x)
            if isPentagonal(p + p2) and isPentagonal (p - p2):
                return -(p2 - p)

tt1 =  datetime.datetime.now()
print('Answer: ', p44())
tt2 =  datetime.datetime.now()
print('Execute time: ', tt2 - tt1) #2.5 seconds
