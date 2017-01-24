from common import count, gcd

def _pow_mod(a, d, n):
    '''a**d % n'''
    b = 1
    a = a % n
    while d:
        if d & 1: b = (b * a) % n
        a = (a * a) % n
        d >>= 1
    return b

def _test_composite(n, s, d, a):
    # return a**d % n != 1 and all(a**(2**r * d) % n != n-1 for r in range(s))
    b = _pow_mod(a, d, n)    # b = a**d % n
    if b == 1: return False
    for r in range(s):
        # b = a**(2**r * d) % n
        if b == n-1: return False   # may be prime
        b = b**2 % n
    return True

def _random_base(n):
    from random import randrange
    return [randrange(2, n) for i in range(50)]
    
def _switch_base(n):
    if n < 2047: return 2,
    if n < 1373653: return 2, 3
    if n < 9080191: return 31, 73
    if n < 25326001: return 2, 3, 5
    if n < 3215031751: return 2, 3, 5, 7
    if n < 4759123141: return 2, 7, 61
    if n < 1122004669633: return 2, 13, 23, 1662803
    if n < 2152302898747: return 2, 3, 5, 7, 11
    if n < 3474749660383: return 2, 3, 5, 7, 11, 13
    if n < 341550071728321: return 2, 3, 5, 7, 11, 13, 17
    if n < 3825123056546413051: return 2, 3, 5, 7, 11, 13, 17, 19, 23
    if n < 18446744073709551616: return 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
    if n < 318665857834031151167461: return 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
    if n < 3317044064679887385961981: return 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41
    return _random_base(n)

def isMRPrim(n):
    if n <= 2: return n == 2
    if n % 2 == 0: return False
    s, d = 0, n-1
    while d % 2 == 0:
        d //= 2
        s += 1
    # print("%d = 2 ** %d * %d + 1" % (n, s, d))
    return all(not _test_composite(n, s, d, a) for a in _switch_base(n))
