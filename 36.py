'''

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

'''
import itertools
import datetime
max = 999999

def get_palindromes():
    palindromes = []
    digits = [str(x) for x in range(10)]
    for cant in range(1, 4):
        palindromes += get_partial_palindromes(cant)
    return palindromes

def get_partial_palindromes(cant):
    digits = [str(x) for x in range(10)]
    palindromes = []
    for item in itertools.product(digits, repeat=cant):
        if item[0] == '0': continue
        if cant < 3:
            for digit in digits:
                palindrome = int(''.join(item) + digit + ''.join([item[x] for x in range(cant - 1, -1, -1)]))
                palindromes.append(palindrome)
        palindrome = int(''.join(item) + ''.join([item[x] for x in range(cant - 1, -1, -1)]))
        palindromes.append(palindrome)
    return palindromes

def isPalindrom(num):
    n = str(bin(num))[2:]
    tam = len(n) // 2
    rev = ''.join(n[x] for x in range(-1, -tam-1,-1))
    if n[:tam] == rev:
        return True
    return False

def p36():
    total = 0
    palindromes = [x for x in range(1, 10)]
    palindromes += get_palindromes()
    for n in palindromes:
        if isPalindrom(n):
            total += n
    return total

tt1 = datetime.datetime.now()

print('Answer: {}'.format(p36())) # 872187

tt2 = datetime.datetime.now()

print('Time: {}'.format(tt2 - tt1)) # 0.01 second

