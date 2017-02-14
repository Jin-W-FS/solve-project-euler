from common import count, lru_cache, Factorize, Divisors

from math import sqrt
def isSquare(v):
    q = sqrt(v)
    return q if q == int(q) else None

Factorize = lru_cache(10)(Factorize)
def findDs(x):
    factors = Factorize(x-1) + Factorize(x+1)
    D = 1
    for k in list(factors.keys()):
        v = factors[k]
        q, r = divmod(v, 2)
        if r == 1:
            D *= k
            if v == 1:
                del factors[k]
            else:
                factors[k] = q
        else:
            factors[k] = q
    if not factors:
        return [D]
    else:
        return [D * f for f in Divisors(factors)]

x, values = 2, { x for x in range(1, 1001) if not isSquare(x) }
def run():
    global x, values
    for x in count(x):
        #print(x)
        for d in findDs(x):
            if d <= 1000: values.discard(d)
            else: break
        if len(values) <= 1: break
    print(values)

run()
