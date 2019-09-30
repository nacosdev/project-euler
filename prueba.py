
import time
import numba

@numba.njit
def p179():
    """ Consecutive positive divisors """
    n = 10**7
    count = 0
    div = [0] * (n+1)
    for i in range(2, n):
        if div[i] == div[i+1]:
            count += 1
        for j in range(2*i, n+1, i):
            div[j] += 1
    return count

if __name__ == "__main__":
    start = time.time()
    r = p179()
    end = time.time()
    print(f"R:{r} in {end-start}s")

    start = time.time()
    r = p179()
    end = time.time()
    print(f"R:{r} in {end-start}s")
