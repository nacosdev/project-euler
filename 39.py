'''

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

'''

from collections import defaultdict
import math, datetime

def p39(maximo = 1000):
    """
    Se van quemando sin repetición todas todas las combinaciones de a^2 + b^2 = c^2 hasta que a + b + c sea mayor al máximo, en este caso 1000
    Por cada nueva combinacion, se cuenta como una nueva solucion para el resultado de su suma en el defaultdict de tipo int, llamado 'results'
    """
    results = defaultdict(int)
    for a in range(1, maximo):
        for b in range(a + 1, maximo):
            c = math.sqrt((a ** 2) + (b ** 2))
            p = a + b + c
            if c.is_integer() == False:
                continue
            if p <= maximo:
                results[int(p)] += 1
            else:
                break
    return max(results, key=results.get) # Devuelve la key con el value maximo-

tt1 = datetime.datetime.now()

print('Answer: ',p39()) # 840

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.3 seconds