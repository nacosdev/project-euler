'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import datetime


def p30():
    sumas = []
    for x in range(2, 1000000):
        suma = 0
        for n in str(x):
            suma += int(n) ** 5
        if x == suma:
            sumas.append(suma)
    return sum(sumas)
tt1 = datetime.datetime.now()

print(p30())

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) #3 seconds