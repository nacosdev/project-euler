'''

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these
divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220,
forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.

'''
from collections import defaultdict
import datetime, math



def d(n):
    inc = 1
    start = 2
    if n % 2 != 0:
        start = 3
        inc = 2
    nums = set(())
    for x in range(start, int(math.sqrt(n) + 1), inc):
        if (n % x) == 0:
            nums.add(x)
            nums.add(n // x)
    return sum(nums) + 1





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
print('Tardo {}.'.format(tt2-tt1))

