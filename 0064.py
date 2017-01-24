from math import sqrt, floor
from fractions import Fraction

def expandSqrt(N):
    sqrtN = sqrt(N)
    m0 = floor(sqrtN)   # sqrt(N) = m0 + (sqrt(N) - m0)
    if m0**2 == N: return m0, ()
    l, r = [], (Fraction(1), Fraction(-m0))
    r0 = r
    def _trans(a, b):
        '''transform 1 < (a*sqrt(N) + b) < 1 to 1/(m + X), which 0 < X = (a', b') < 1'''
        # m = floor(1 / (a*sqrt(N) + b)) = floor((a*sqrt(N) - b) / (a**2 * N - b**2))
        m = floor(1 / (float(a)*sqrtN + b))
        d = a**2 * N - b**2
        return m, (a/d, -b/d - m)
    while True:
        m, r = _trans(*r)
        l.append(m)
        if r == r0: return m0, l

N = 10000
print(sum(len(expandSqrt(i)[1]) % 2 for i in range(N+1)))
