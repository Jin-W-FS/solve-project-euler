# C(n-x, n) = C(x, n)
# C(x, n+1) = C(x-1, n) + C(x, n)
# C(0, n) = 1

from common import Comb

r, n = 9, 23
# lower = [(r, n)]
s = n-2*r-1
for n in range(24, 101):
    while Comb(r, n) > 1000000:
        r -= 1
    # lower.append((r, n))
    s += n-2*r-1

print(s)

