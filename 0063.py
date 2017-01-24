'''require: 10**(n-1) <= a**n < 10**n,
so a < 10, and N = max(n) has 10**(N-1) <= 9**N, N <= 1 / (1 - log10(9))'''

from math import log10, floor

N = floor(1 / (1 - log10(9)))

cnt = 0
for n in range(1, N+1):
    m0 = 10**(n-1)
    m1 = 10*m0
    for a in range(1, 10):
        if m0 <= a**n < m1:
            print(a, n)
            cnt += 1
print(cnt)

