import datetime
def is_prime(num):
    if num < 3 or num % 2 == 0:
        return (num == 2)
    else:
        return all(num % i != 0 for i in range(3, int(num**0.5 + 2), 2))

def p58():
    offset = 2
    pre = 2
    rounds = 0
    counter = 0
    counter_primes = 0
    x = 1
    lent = 0
    while True:
        if is_prime(x):
            counter_primes += 1
        counter += 1
        pre = 0
        if rounds == 4:
            lent += 1
            offset += 2
            rounds = 0
        rounds += 1
        pre += 1
        x +=  offset
        if counter_primes / counter < 0.1 and counter_primes > 0 :
            break

    return (lent * 2) + 1
    print(lent)

    #return counter_primes / counter
tt1 = datetime.datetime.now()
print('Answer: ',p58())
tt2 = datetime.datetime.now()
print('Time: ', tt2 - tt1) # 9 Seconds







'''viejo
def p58(len_spiral):
    offset = 2
    pre = 2
    rounds = 0
    counter = 0
    counter_primes = 0
    x = 1
    lent = 1
    while x <= len_spiral ** 2:
    #while True:
        if pre == offset:
            print(x)
            counter += 1
            if is_prime(x):
                counter_primes += 1
            pre = 0
            if rounds == 4:
                lent += 1
                offset += 2
                rounds = 0
            rounds += 1
        pre += 1
        x +=  1
        #print(counter_primes / counter)

    return counter_primes / counter
'''

