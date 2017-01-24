from itertools import count
from common import Counter, lru_cache, Factorize

def CountFacts(d):
    m = 1
    for v in d.values():
        m *= (v + 1)
    return m

Factorize = lru_cache(maxsize=None)(Factorize)

for i in count(2):
    # n = (i-1)*i//2
    d0 = Factorize(i-1)
    d1 = Factorize(i)
    d = Counter(d0)
    d.update(d1)
    d[2] -= 1
    c = CountFacts(d)
    if c > 500: break

print(i, (i-1)*i//2, d, c)

