from common import count, isPrim, Factorize3

def countFacts(n):
    if isPrim(n): return 1
    return len(Factorize3(n))

N = 4
lst = []
for n in count(1):
    if countFacts(n) == N:
        lst.append(n)
        if len(lst) == N: break
    else:
        lst.clear()
print(lst)

