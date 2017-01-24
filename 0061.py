from collections import defaultdict
from itertools import chain, count

def pset(gntr):
    d = defaultdict(set)
    for n in count(1):
        v = gntr(n)
        if v < 1000: continue
        if v >= 10000: break
        s = str(v)
        d[int(s[0:2])].add(int(s[2:4]))
    return d

pols = [
    pset(lambda n: n*(n+1)//2),
    pset(lambda n: n**2),
    pset(lambda n: n*(3*n-1)//2),
    pset(lambda n: n*(2*n-1)),
    pset(lambda n: n*(5*n-3)//2),
    pset(lambda n: n*(3*n-2))
    ]

def search(k0, k, S):
    'depth-first search, now pols[i] key k'
    # print(' '*i, k, sep='')
    if not S:
        return [] if k0 == k else None
    for s in S:
        R = [e for e in S if e != s]
        for v in s[k]:
            rlt = search(k0, v, R)
            if rlt is not None: return [v] + rlt
    return None

def combine(lst):
    return [lst[i-1]*100 + lst[i] for i in range(len(lst))]
    
starting = set(chain.from_iterable(pols[-1].values()))
for k in starting:
    r = search(k, k, pols)
    if r: break
rlt = combine(r)
print(rlt, sum(rlt))
