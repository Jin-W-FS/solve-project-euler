from itertools import count

def Triangle():
    for n in count(1):
        yield n * (n+1) // 2

def Pentagonal():
    for n in count(1):
        yield n * (3*n-1) // 2
        
def Hexagonal():
    for n in count(1):
        yield n * (2*n-1)


iters = [Triangle(), Pentagonal(), Hexagonal()]
cur = [next(it) for it in iters]

def loop():
    while not all(v == cur[0] for v in cur[1:]):
        k = min(range(len(cur)), key=lambda i: cur[i])
        cur[k] = next(iters[k])
    rlt = cur[0]
    cur[0] = next(iters[0])
    return rlt

print(loop(), loop(), loop())
