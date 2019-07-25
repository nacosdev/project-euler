import json


'''
A natural number, N, that can be written as the sum and product of a given set of at least two natural numbers, {a1, a2, ... , ak} is called a product-sum number: N = a1 + a2 + ... + ak = a1 × a2 × ... × ak.

For example, 6 = 1 + 2 + 3 = 1 × 2 × 3.

For a given set of size, k, we shall call the smallest N with this property a minimal product-sum number. The minimal product-sum numbers for sets of size, k = 2, 3, 4, 5, and 6 are as follows.

k=2: 4 = 2 × 2 = 2 + 2
k=3: 6 = 1 × 2 × 3 = 1 + 2 + 3
k=4: 8 = 1 × 1 × 2 × 4 = 1 + 1 + 2 + 4
k=5: 8 = 1 × 1 × 2 × 2 × 2 = 1 + 1 + 2 + 2 + 2
k=6: 12 = 1 × 1 × 1 × 1 × 2 × 6 = 1 + 1 + 1 + 1 + 2 + 6

Hence for 2≤k≤6, the sum of all the minimal product-sum numbers is 4+6+8+12 = 30; note that 8 is only counted once in the sum.

In fact, as the complete set of minimal product-sum numbers for 2≤k≤12 is {4, 6, 8, 12, 15, 16}, the sum is 61.

What is the sum of all the minimal product-sum numbers for 2≤k≤12000?
'''

import math, datetime
kmax = 12000

deph = kmax + 1
if kmax > 999:
    deph = int(kmax * 0.04)
stop = (kmax * 2) + 1
ks = {}

def find_mins(multipliers):
    #print(multipliers)
    prod = 1
    for n in multipliers:
        prod *= n
    k = (prod - sum(multipliers)) + len(multipliers)
    if prod < stop:
        if k < kmax + 1:
            if k in ks:
                if prod < ks[k]:
                    ks[k] = prod
            else:
                ks[k] = prod
        new_multipliers = []
        if (prod * 2) <= stop:
            new_multipliers = multipliers.copy()
            new_multipliers.append(2)
            find_mins(new_multipliers)
        new_multipliers_aux = multipliers.copy()
        new_multipliers_aux[-1] += 1
        new_prod = 1
        for n in new_multipliers_aux:
            new_prod *= n
        if new_prod < stop:
            if new_multipliers_aux[-1] < deph:
                find_mins(new_multipliers_aux)

tt1 = datetime.datetime.now()
find_mins([2])
set_ps = set(())
for v in ks.values():
    set_ps.add(v)
print(sum(set_ps) - 2)
tt2 = datetime.datetime.now()
print('Preformance: ',(tt2-tt1) )

