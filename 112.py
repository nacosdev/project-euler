'''

Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just over half of the numbers below one-thousand (525) are bouncy. In fact,
the least number for which the proportion of bouncy numbers first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is exactly 99%.

'''


import datetime

def is_bouncy(n):
    s_n = str(n)
    n = 0
    tipo = None #True for increasing; False for decreasing
    for x in range(0, len(s_n) - 1):
        if tipo == True:
            if int(s_n[x] > s_n[x + 1]):
                return True
        if tipo == False:
            if int(s_n[x] < s_n[x + 1]):
                return True
        if tipo == None:
            if int(s_n[x] == s_n[x + 1]):
                continue
            if int(s_n[x] < s_n[x + 1]):
                tipo = True
            else:
                tipo = False
    return False

def p112():
    boun = 0
    total = 100
    x = 101
    while True:
        if is_bouncy(x):
            boun += 1
        total += 1
        if (boun / total) >= 0.99:
            return x
        #print('Percentaje: ', boun / total)
        x += 1

tt1 = datetime.datetime.now()

print('Answer: ',p112())

tt2 = datetime.datetime.now()

print('Execute time: ', tt2 - tt1) #3.4 seconds
