'''

For any set A of numbers, let sum(A) be the sum of the elements of A.
Consider the set B = {1,3,6,8,10,11}.
There are 20 subsets of B containing three elements, and their sums are:

sum({1,3,6}) = 10,
sum({1,3,8}) = 12,
sum({1,3,10}) = 14,
sum({1,3,11}) = 15,
sum({1,6,8}) = 15,
sum({1,6,10}) = 17,
sum({1,6,11}) = 18,
sum({1,8,10}) = 19,
sum({1,8,11}) = 20,
sum({1,10,11}) = 22,
sum({3,6,8}) = 17,
sum({3,6,10}) = 19,
sum({3,6,11}) = 20,
sum({3,8,10}) = 21,
sum({3,8,11}) = 22,
sum({3,10,11}) = 24,
sum({6,8,10}) = 24,
sum({6,8,11}) = 25,
sum({6,10,11}) = 27,
sum({8,10,11}) = 29.

Some of these sums occur more than once, others are unique.
For a set A, let U(A,k) be the set of unique sums of k-element subsets of A, in our example we find U(B,3) = {10,12,14,18,21,25,27,29} and sum(U(B,3)) = 156.

Now consider the 100-element set S = {1^2, 2^2, ... , 100^2}.
S has 100891344545564193334812497256 50-element subsets.

Determine the sum of all integers which are the sum of exactly one of the 50-element subsets of S, i.e. find sum(U(S,50)).

'''
import itertools

#print([x**2 for x in range(1,101)])

def p201_ejemplo():
    S = [1,3,6,8,10,11]
    repeated = set(())
    sumas = set(())
    for item in itertools.combinations(S, 3):
        suma = sum(item)
        if suma in repeated:
            continue
        if suma in sumas:
            repeated.add(suma)
            sumas.remove(suma)
            continue
        sumas.add(suma)
    return sum(sumas)


def is_unique(S, k, x):
    unique = False
    


def p201(S = [1,3,6,8,10,11], k = 3):
    mini = sum(S[:k])
    maxi = sum(S[-k:])
    for x in range(mini+1, maxi):
        suma = 0
        for x in range(k):
            pass

    print(mini, maxi)
print(p201())

Lista = [x**2 for x in range(1, 101)]
last = 0
for item in Lista:
    diferencia = item - last
    last = item
    print(item, diferencia)


asd = [0,1,2]
for item in itertools.permutations(asd):
    print(item)


