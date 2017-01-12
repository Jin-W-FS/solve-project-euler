from common import prim, prims, isPrim


def count(a, b):
    n = 1
    while True:
        p = n*n + a*n + b
        if p <= 0 or not isPrim(p):
            return n
        n += 1

def prims_le(n):
    for p in prims():
        if p > n: break
        yield p


m = (0, 0, 0)
for b in prims():
    if b > 1000: break
    for a in range(-999, 1000):
        c = count(a, b)
        if c > m[0]: m = (c, a, b)
print(m)
