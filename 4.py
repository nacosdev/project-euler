def is_palindrome(n):
    n = str(n)
    if len(n)<2: return False
    if n == n[::-1]:return True
    return False
def find_max_palindrome(n_digits):
    palindrome_max = 0
    digits = int('1'+''.join(['0' for item in range(0,n_digits)]))
    for x in range(1,digits):
        for y in range(1,digits):
            n = x*y
            if (is_palindrome(n) and n > palindrome_max):
                 palindrome_max = n
    return palindrome_max

print(find_max_palindrome(4))