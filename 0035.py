from common import prims_lt

prims = list(prims_lt(1000000))
primset = set(prims)

def primRotSet(p):
    k = len(str(p)) - 1
    s = {p}
    if k == 0:
        return s
    def shift(n):
        q, r = divmod(n, 10**k)
        return q + r * 10
    n = shift(p)
    while n != p:
        if n % 2 == 0:
            return None
        s.add(n)
        n = shift(n)
    return s

rlt = set()
for p in prims:
    if p in rlt: continue
    s = primRotSet(p)
    if s and s.issubset(primset):
        rlt.update(s)

# for p in sorted(rlt): print(p)
print(len(rlt))

