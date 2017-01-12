from common import initPrimCache, isPrim, Arranges

initPrimCache(10**4)
bases = [range(7,0,-1), range(4,0,-1)]

def cmbint(l):
    r = 0
    for d in l:
        r = r * 10 + d
    return r

def test():
    for base in bases:
        for lst in Arranges(base):
            n = cmbint(lst)
            if isPrim(n):
                return n

print(test())
