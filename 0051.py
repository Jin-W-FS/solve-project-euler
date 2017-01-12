# as x | 3 <=> sum(d in x) | 3
# by replace 3n+1 or 3n+2 digit in x we can generate at most 10-3 prims

from common import prims, isPrim, digits
from collections import Counter

def replacements(x):
    s = str(x)
    c = Counter(s)
    for d, n in c.most_common():
        if n < 3: return []
        if n % 3 != 0: continue
        yield [int(x) for x in
               (s.replace(d, i) for i in '0123456789')
               if x[0] != '0']

def test():
    for p in prims():
        if p < 1000: continue
        for it in replacements(p):
            n = len(it)
            for x in it:
                if not isPrim(x):
                    n -= 1
                if n < 8:
                    break
            else:
                return p

print(test())


