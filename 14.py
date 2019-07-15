from collections import defaultdict
import datetime
'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''
dict_cache = {}
def Collatz(n):
    terms = 0
    key = str(n)
    while n is not 1:
        if str(n) in dict_cache:
            terms += dict_cache[(str(n))]
            break
        terms += 1
        if (n % 2) is 0:
            
            n = n//2
        else:
            n = (n*3) + 1
    dict_cache[key] = terms
    return terms
longest = 0
longest_term = 0
tt1 = datetime.datetime.now()
for n in range(1, 1000000):
    chain = Collatz(n)
    if chain > longest:
        longest = chain
        longest_term = n
print(longest_term)
print('It took {} seconds'.format((datetime.datetime.now()-tt1).seconds))
