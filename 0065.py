from fractions import Fraction
from math import ceil
from common import digits

def combine(vec):
    m, l = vec
    v = float('inf')
    for x in reversed(l):
        v = Fraction(x + 1 / v)
    v = Fraction(m + 1 / v)
    return v

def e_seq(n):
    m, l = 2, []
    for i in range(1, ceil((n-1)/3)+1):
        l.extend([1, 2*i, 1])
    l = l[:n-1]
    assert(len(l) == n-1)
    return m, l

f = combine(e_seq(100))
print(sum(digits(f.numerator)))

