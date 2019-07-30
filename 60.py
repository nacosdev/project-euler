'''

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order
the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

'''
import math, itertools, datetime
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))



def p60(deph, ps, rmks):
    for i, p in enumerate(ps):
        str_p = str(p)
        nw_rmks = rmks.copy()
        nw_rmks.append(str_p)
        if is_remarkable(nw_rmks):
            if len(nw_rmks) == deph:
                print('rmks', nw_rmks)
                return sum([int(x) for x in nw_rmks])
            else:
                is_end = p60(deph, ps[i+1:], nw_rmks)
                if is_end:
                    return is_end

def is_remarkable(ns):
    for com in itertools.permutations(ns,2):
        if sum(int(n) for n in com) % 3 == 0: return False
        n = int(''.join([i for i in com]))
        if not is_prime(n):
            return False
    return True


tt1 = datetime.datetime.now()

primes = prime_sieve(10000)
print(p60(5,primes,[]))

tt2 = datetime.datetime.now()

print('Total time: ', tt2 - tt1)