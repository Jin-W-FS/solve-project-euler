
factorials = [1] * 10
for i in range(1, 10): factorials[i] = factorials[i-1] * i

cache = {
    169 : 3, 363601 : 3, 1454 : 3,
    871 : 2, 45361 : 2, 872 : 2, 45362: 2,
}

def nextn(n):
    s = 0
    while n:
        n, r = divmod(n, 10)
        s += factorials[r]
    return s

def nrterms(n):
    c = cache.get(n)
    if c is not None: return c
    nn = nextn(n)
    if nn == n:
        c = 1
    else:
        c = 1 + nrterms(nn)
    cache[n] = c
    return c

c = 0
for n in range(1000000):
    if nrterms(n) == 60:
        c += 1
        print(n)
print("Total:",  c)
