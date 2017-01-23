from common import IncSerial, Prims, count

twicesqare = IncSerial([], lambda l: 2*len(l)**2)

odds = [2*i+3 for i in range(10000)]
MAX = odds[-1]

for p in Prims:
    if p == 2: continue
    if p > MAX: break
    for q in twicesqare:
        if q > MAX: break
        s = p + q
        if s > MAX: break
        odds[(s-3)//2] = 0

for n in filter(None, odds): print(n)

