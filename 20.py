'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''


def factor(n):
    f = 1
    for x in range(n, 0, -1):
        f *= x
    return f

def p20(num):
    return sum([int(n) for n in str(factor(num))])

print(p20(100))


