'''

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits,
but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

'''
import itertools

'''
Se hizo basandose en que cualquier numero que comienze con alguna combinacion igual o más grande que 17xxxxxx, al multiplicarse por 6 
se genera otra cifra, por lo que nunca van a ser iguales, dado este se reduce enormemente el número de posibilidades a comprobar
'''
def p52():
    for item in itertools.permutations(['1','2','3','4','5','6'], 1):
        for x in range (1, 10000):
            
            n1 = int('1'+ item[0] + str(x))
            ordered_1 = ''.join(sorted(str(n1)))
            for muls in range(2, 7):
                is_equal = False
                n2 = n1 * muls
                ordered_2 = ''.join(sorted(str(n2)))
                if ordered_1 == ordered_2:
                    is_equal = True
                else:
                    is_equal = False
                    break
            if is_equal:
                return n1
    
print(p52())