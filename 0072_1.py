from common import prim_factors_lt
from functools import reduce

N = 1000000
facs = prim_factors_lt(N+1)

def subsets(lst):
    for k in range(2**len(lst)):
        yield [lst[i] for i in range(len(lst)) if (k & (1<<i))]

def product(lst):
    return reduce(int.__mul__, lst, 1)

def fai(n):
    '''len([x for x in range(1, n) if n % x != 0])'''
    return sum((-1)**len(ss) * (n // product(ss)) for ss in subsets(facs[n]))


s = sum(fai(i) for i in range(2, N+1))
print(s)
