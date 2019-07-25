from collections import defaultdict
import datetime
'''

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

'''


def d(n):
    return sum([x for x in range(1, ((n + 1) // 2) + 1) if n % x == 0])

def p21(maxx):
    dict_sums = defaultdict(int)
    for x in range(1, maxx + 1):
        dict_sums[x] = d(x)
    amicables = []
    for k in dict_sums:
        if dict_sums[k] != k:
            if dict_sums[k] in dict_sums:
                if dict_sums[dict_sums[k]] == k:
                    amicables.append(k)

    return sum(amicables)


tt1 = datetime.datetime.now()
print(p21(10000))
tt2 = datetime.datetime.now()
print('Tardo {} segundos.'.format((tt2-tt1).seconds))


