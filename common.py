def Factorize(y):
    f = []
    p = prims()
    x = next(p)
    while y > 1:
        while y % x != 0:
            x = next(p)
        f.append(x)
        y = y // x
    return f

# print(Factorize(600851475143))

from collections import Counter
def Factorize2(y):
    f = Counter()
    x = 2
    while y > 1:
        while y % x != 0:
            x += 1
        f[x] += 1
        y = y // x
    return f

def Factorize3(y):
    f = Counter()
    p = prims()
    x = next(p)
    while y > 1:
        while y % x != 0:
            x = next(p)
        f[x] += 1
        y = y // x
    return f

def ProperDivisors(x):
    d = [1]
    for i in range(2, x):
        i2 = i * i
        if i2 > x:
            break
        elif i2 == x:
            d.append(i)
            break
        else:
            if x % i == 0:
                d.extend((i, x // i))
    return d

# print(Factorize2(999999))

from functools import lru_cache

@lru_cache(maxsize=None)
def fib(i):
    if i < 2: return 1
    return fib(i - 1) + fib(i - 2)

def fibN(i):
    from math import sqrt
    sqrt5 = sqrt(5)
    a = (1 + sqrt5) / 2
    return round(a ** i / sqrt5)

from itertools import count
_prim_cache = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]
def _inPrimCache(n, cache):
    from bisect import bisect_left
    i = bisect_left(cache, n)
    return 0 <= i < len(cache) and cache[i] == n

def _isPrim(n, cache):
    for p in cache:
        if p**2 > n: return True
        if n % p == 0: return False
    raise RuntimeError("shouldn't reach here")

def _nextPrim(cache):
    if len(cache) < 2:
        return 2 if not cache else 3
    for n in count(start=cache[-1]+2, step=2):
        if _isPrim(n, cache): return n

def initPrimCache(n):
    global _prim_cache
    _prim_cache = list(prims_lt(n))

def prim(i):
    while len(_prim_cache) <= i:
        _prim_cache.append(_nextPrim(_prim_cache))
    return _prim_cache[i]

def prims():
    for i in count(): yield prim(i)

def isPrim(n):
    if n <= _prim_cache[-1]:
        return _inPrimCache(n, _prim_cache)
    for p in prims():
        if p**2 > n:
            return True
        if n % p == 0:
            return False

def prims_lt(N):
    lst = list(range(N))
    lst[0] = lst[1] = 0
    for i in range(N):
        if lst[i] == 0: continue
        x = i+i
        while x < N:
            lst[x] = 0
            x += i
    return filter(None, lst)

def prim_factors_lt(N):
    factors = [[] for i in range(N)]
    for i in range(2, N):
        if factors[i]: continue
        k = i
        while k < N:
            factors[k].append(i)
            k += i
    return factors

def adjacent_product_max(l, n):
    '''max product of N adjacent numbers in l'''
    if len(l) < n: return 0
    def product(lst):
        from functools import reduce
        return reduce(int.__mul__, lst, 1)
    mp = mc = product(l[:n])
    for i in range(n, len(l)):
        if l[i-n] == 0:
            mc = product(l[i-n+1:i+1])
        else:
            mc = mc // l[i-n] * l[i]            
        if mc > mp: mp = mc
    return mp

def digits(n):
    while n:
        n, r = divmod(n, 10)
        yield r

def lstdigits(init, base=10):
    lst = list(init)
    while True:
        yield lst
        lst[-1] += 1
        for i in reversed(range(len(lst))):
            if lst[i] == base:
                if i == 0: return
                lst[i] = 0
                lst[i-1] += 1

def cmbdigits(lst, base=10):
    s = 0
    for n in lst: s = s * base + n
    return s

def palindromics(length, base=10):
    '''those reads the same from both side, of length length, under base base'''
    assert(length > 0)
    n = (length + 1) // 2 # length = 2n | 2n - 1
    vec = [0] * length
    init = [1] + [0] * (n-1)
    for lst in lstdigits(init, base):
        vec[:n] = lst
        vec[-n:] = reversed(lst)
        yield cmbdigits(vec, base)

@lru_cache(maxsize=None)
def Comb(r, n):
    if r == 0 or r == n: return 1
    return Comb(r-1, n-1) + Comb(r, n-1)

def gcd(a, b):
    if a > b: a, b = b, a
    while a != 0:
        a, b = b % a, a    
    return b

def totient(n):
    '''sum((gcd(i, n) == 1) for i in range(1, n))
    n * product((1 - 1/p) for n | p)
    https://en.wikipedia.org/wiki/Euler%27s_totient_function'''
    if n <= 2: return 0
    facts = Factorize3(n)
    for p in facts:
        n = n // p * (p - 1)
    return n

def totients_lt(N):
    primfact = [0] * (N+1)  # mark one factor like p**k
    totients = [0] * (N+1)

    def mark_prim_rates_pow(p):
        pk0, pk = 1, p
        while pk < N+1:
            totients[pk] = pk - pk0
            for n in range(pk*2, N+1, pk):
                primfact[n] = pk
            pk0, pk = pk, pk * p

    for i in range(2, N+1):
        if primfact[i] == 0:    # is prim
            mark_prim_rates_pow(i)
        elif totients[i] == 0:
            p = primfact[i]
            totients[i] = totients[p] * totients[i // p]

    return totients

def Arranges(base):
    def ArrangeInc(l):
        c = 1
        for j in range(len(l)):
            idx, thd = -1-j, j+1
            l[idx] += c; c = 0
            if l[idx] >= thd:
                l[idx] -= thd; c = 1
            if c == 0:
                break
        return c
    def SwitchElemsLitera(l, base):
        base = list(base)
        return [base.pop(d) for d in l]
    base = list(base)
    l = [0] * len(base)
    c = 0
    while not c:
        yield SwitchElemsLitera(l, base)
        c = ArrangeInc(l)
