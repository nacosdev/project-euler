'''

It is easily proved that no equilateral triangle exists with integral length sides and integral area. However, the almost equilateral triangle 5-5-6
has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths and area and whose perimeters do not exceed one billion (1,000,000,000).

'''
import math

#def p(a):
    #return((a + a + a + 1) / 2)

def area(a, p):
    return math.sqrt(p*(p-a)*(p-a)*(p-(a + 1)))

def p94():
    suma = 0
    x = 2
    while x < 1000000:
        per = (x * 3) + 1
        p = (per / 2)
        multi = p*((p-x) ** 2) * (p - (x + 1))
        are = math.sqrt(multi)
        #are = area(x, p)
        if are.is_integer():
            print(x, are, per, multi)
            suma += p
        x += 1
    return suma
print(p94())

def hallar_p(x):
    side = ((((x * 3) + 1) / 2)*(((((x * 3) + 1) / 2)-x) ** 2) * ((((x * 3) + 1) / 2) - (x + 1)))

# power = p * (p-a) * (p-a) * (p - ( a + 1 ))

def p94_opti():
    suma = 0
    x = 1
    while x < 1000000:
        power = x ** x
        if (power % 3) == 1:
            side = power // 3