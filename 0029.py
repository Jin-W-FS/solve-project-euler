
N = 100

from collections import Counter
from common import lru_cache

@lru_cache()
def duplicated(p):
    cnt = Counter()
    l = range(1, p+1)
    cnt.update(n * x for x in l for n in range(2, N+1))
    return sum(cnt.values()) - len(cnt)

def maxpow(base):
    p, n = 0, base
    while n <= N:
        p += 1
        n *= base
    return p

s = (N-1) * (N-1)
for b in [2, 3, 5, 6, 7, 10]:
    p = maxpow(b)
    if p == 1: break
    d = duplicated(p)
    print(b, p, d)
    s -= d
    b += 1

print(s)

