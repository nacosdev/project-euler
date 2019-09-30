'''

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

'''
from collections import defaultdict
import datetime

def p76(hasta = 100):
    dict_cache = defaultdict(int)
    dict_cache[0] += 1
    for x in range(1, hasta):
        for y in range(x, hasta + 1):
            dict_cache[y] += dict_cache[y - x]
    return dict_cache[hasta]

tt1 = datetime.datetime.now()

print('Answer: ', p76(100)) # 190569291

tt2 = datetime.datetime.now()

print('Time: ', tt2 - tt1) # 0.001 second


'''
7
6 + 1
5 + 2
5 + 1 + 1
4 + 3
4 + 2 + 1
4 + 1 + 1 + 1
3 + 3 + 1
3 + 2 + 2
3 + 2 + 1 + 1
3 + 1 + 1 + 1 + 1
2 + 2 + 2 + 1
2 + 2 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1

6
5 + 1
4 + 2
4 + 1 + 1
3 + 3
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 2
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1

5
4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1



3 + 3 + 3 + 1
3 + 3 + 2 + 2
3 + 3 + 2 + 1 + 1
3 + 3 + 1 + 1 + 1 + 1
3 + 2 + 2 + 2 + 1
3 + 2 + 2 + 1 + 1 + 1
3 + 2 + 1 + 1 + 1 + 1 + 1
3 + 1 + 1 + 1 + 1 + 1 + 1 + 1
2 + 2 + 1 + 1 + 1 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1


'''
