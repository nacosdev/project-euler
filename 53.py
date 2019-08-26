import datetime

def factorial(n):
    init = 1
    for x in range(1, n + 1):
        init *= x
    return init

def combinatorics(n, r):
    return factorial(n) / (factorial(r) * factorial(n - r))

#print(combinatorics(23, 10))

def p53(below):
    suma = 0
    for x in range(0, below + 1):
        for y in range(1, x + 1):
            if combinatorics(x, y) > 1000000:
                suma += 1
    return suma

tt1 = datetime.datetime.now()

print('Answer: ',p53(100)) # 4075

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.07 seconds