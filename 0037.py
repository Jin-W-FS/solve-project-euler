from common import prims, isPrim

def check(p):
    if p < 10: return False
    s = str(p)
    prims1 = {2, 3, 5, 7}
    if not (int(s[0]) in prims1 and int(s[-1]) in prims1):
        return False
    for i in range(1, len(s)):
        d, r = divmod(p, 10**i)
        if not (isPrim(d) and isPrim(r)):
            return False
    return True

s, n = 0, 0
for p in prims():
    if check(p):
        print(p)
        s += p
        n += 1
        if n == 11: break
print('s =', s)
