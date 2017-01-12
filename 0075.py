from math import *

N = 1500000

d = {}
for m in range(1, floor(sqrt(N/2))+1):
    for n in range(1, m):
        a, b, c = m**2-n**2, 2*m*n, m**2+n**2
        if a >= b: a, b = b, a
        s = a + b + c
        for k in range(1, floor(N/s)+1):
            d[(k*a, k*b, k*c)] = k*s
c = [0] * (N+1)
for v in d.values():
    c[v] += 1
print(c.count(1))


