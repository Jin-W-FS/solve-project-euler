'''like 0046, do a real search in real number domain'''

from common import IncSerial, Prims, count, sortedlist

odds = sortedlist([1], unique=True) # may be better using binary sort tree

for s in count(1): # iter through i + j == s
    m = None # minimal of this loop
    for i in range(1, s+1):
        j = s - i
        p, q = Prims[i], twicesqare[j]
        n = p + q
        odds.insert(n)
        if m is None or n < m: m = n
    cnt = odds.index_gt(m)
    if cnt < (m + 1) / 2: break

for i in range(1, cnt):
    odd = odds[i-1] + 2
    if odd != odds[i]:
        print(odd)


