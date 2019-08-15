'''

Lattice paths

'''
from collections import defaultdict
import datetime

#Esto fue resuelto con programacion dinamica, primero resolviendo pequeños casos, y sumando los resultados parciales, ya que con fuerza bruta no terminara de ejecutar nunca

dict_sums = defaultdict(lambda: defaultdict(int))

def p15(length):
    for x in range(1, length + 1):
        paths(x,x)
    return dict_sums[length][length]

def paths(right, down):
    pts = 0
    if right == 0 or down == 0:
        return 1
    if right > 0:
        if dict_sums[right - 1][down] != 0:
            pts += dict_sums[right - 1][down]
        elif dict_sums[down][right - 1] != 0:
            pts += dict_sums[down][right - 1]
        else:
            pts += paths(right - 1, down)
    if down > 0:
        if dict_sums[right][ down - 1] != 0:
            pts += dict_sums[right][ down - 1]
        elif dict_sums[ down - 1][right] != 0:
            pts += dict_sums[ down - 1][right]
        else:
            pts += paths(right,  down - 1)
    dict_sums[right][down] = pts
    return pts

tt1 = datetime.datetime.now()

print('Answer: ', p15(20))

tt2 = datetime.datetime.now()

print('Execute time: ', tt2 - tt1) #0.001 seconds