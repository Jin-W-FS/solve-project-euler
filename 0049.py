from common import Prims, digits
from collections import defaultdict

d = defaultdict(list)

for p in Prims:
    if p < 1000: continue
    if p > 10000: break
    k = tuple(sorted(digits(p)))
    if k is None: continue
    d[k].append(p)

def findSeq3(lst):
    rlt = []
    if len(lst) < 3: return rlt
    for i in range(len(lst)-2):
        a0 = lst[i]
        for j in range(i+1, len(lst)-1):
            a1 = lst[j]
            a2 = a1 * 2 - a0
            if a2 in lst[j+1:]:
                rlt.append((a0, a1, a2))
    return rlt

for lst in d.values():
    s = findSeq3(lst)
    if s: print(s)
