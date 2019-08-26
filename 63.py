'''

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

'''

def p63():
    total = 0
    for x in range(1, 100):
        for y in range(1 , 100):
            res = x ** y
            if len(str(res)) == y:
                total += 1
    return total

print('Answer: ',p63())