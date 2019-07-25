'''

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.

'''

def p48(maxx):
    total = 0
    for x in range(1,maxx + 1):
        total += (x**x)
    return str(total)[-10:]

print(p48(1000))