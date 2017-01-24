from common import digits, cmbdigits

def reversedigits(n):
    return cmbdigits(digits(n))

def isPalindromic(n):
    v = list(digits(n))
    return all(x == y for x, y in zip(v, reversed(v)))

def checkLychrel(n):
    for i in range(50):
        n = n + reversedigits(n)
        if isPalindromic(n): return False
    return True

print(sum(checkLychrel(n) for n in range(1, 10000)))
