from collections import Counter
def Factorize(y):
    f = Counter()
    p = prims()
    x = next(p)
    while y > 1:
        while y % x != 0:
            x = next(p)
        f[x] += 1
        y = y // x
    return f

def Divisors(facts):
    if not isinstance(facts, dict): facts = Factorize(facts)
    if not facts: return [1]
    ks, vs = zip(*facts.items())
    return sorted(prod(k**t for k, t in zip(ks, ts)) for ts in Combinations(vs)) 

def ProperDivisors(arg):
    return Divisors(arg)[:-1]

def ProperDivisorsN(x):
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

from functools import reduce
def prod(iterable, start=None):
    '''prod => product of iterable'''
    if start is None:
        return reduce((lambda x, y: x * y), iterable)
    else:
        return reduce((lambda x, y: x * y), iterable, start)

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

class IncSerial:
    '''an unlimited increasing number serial'''
    def __init__(self, initial, genNext):
        self.lst = list(initial)
        self.genNext = genNext
        
    def rebase(self, lst):
        self.lst = list(lst)

    def __getitem__(self, idx):
        while len(self.lst) <= idx:
            self.lst.append(self.genNext(self.lst))
        return self.lst[idx]
    
    def __iter__(self):
        for i in count(): yield self[i]
        
    def __contains__(self, n):
        return self.index(n) is not None

    def index(self, n):
        if self.lst[-1] >= n:
            from bisect import bisect_left
            idx = bisect_left(self.lst, n)
            if (0 <= idx < len(self.lst) and self.lst[idx] == n): return idx
        else:
            while self.lst[-1] < n:
                v = self.genNext(self.lst)
                self.lst.append(v)
                if v == n: return len(self.lst)-1
        # if n not in self:
        return None


def __isPrim(n, lst):
    for p in lst:
        if p**2 > n: return True
        if n % p == 0: return False

def __nextPrim(lst):
    for n in count(start=lst[-1]+2, step=2):
        if __isPrim(n, lst): return n

Prims = IncSerial([2, 3], __nextPrim)

prim = lambda i: Prims[i]
prims = lambda: iter(Prims)
isPrim = lambda n: n in Prims
isPrim2 = lambda n: isPrim(n) if n <= Prims[-1] else __isPrim(n, Prims)
    
def primTable(N):
    lst = [True] * N
    lst[0] = lst[1] = False
    for i in range(N):
        if lst[i]:
            for x in count(i+i, i):
                if x >= N: break
                lst[x] = False
    return lst # lst[n] == isPrim(n)

def prims_lt(N):
    tab = primTable(N)
    return [n for n in range(N) if tab[n]]

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

def Combinations(maxes, includes=True):
    '''generate product vs of which vs[i] is between 0 and maxes[i](includes maxes[i])'''
    from itertools import product
    return product(*(range(m+includes) for m in maxes))

class sortedlist(list):
    def __init__(self, iterable=(), unique=False):
        super().__init__()
        self.unique = unique
        for v in sorted(iterable):
            if self.unique and len(self) and v == self[-1]: continue
            self.append(v)
    def insert(self, item):
        from bisect import bisect_left
        idx = bisect_left(self, item)
        if self.unique and idx < len(self) and self[idx] == item: return
        super().insert(idx, item)
    def index_gt(self, item):
        from bisect import bisect_right
        return bisect_right(self, item)
    def index_ge(self, item):
        from bisect import bisect_left
        return bisect_left(self, item)

def WaysSumToWith(lst):
    @lru_cache(maxsize=None)
    def WaysSumTo(n, i=0):
        '''find out ways to sum to n with element in lst[i:]'''
        if n == 0: return 1
        try: v = lst[i]
        except IndexError: return 0
        if v > n: return 0
        return sum(WaysSumTo(n-k*v, i+1) for k in range(n//v+1))
        # return WaysSumTo(n-v, i) + WaysSumTo(n, i+1)
    return WaysSumTo

