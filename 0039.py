from collections import defaultdict
from itertools import count

# sqrt(1000) < 32
# sqrt(1000/2) < 25
# p = m**2+n**2 + 2*m*n + m**2-n**2 = 2*m*(m+n)
# p = 2*m*(m+n), m > n > 0

counter = defaultdict(set)

for m in range(2, 23):
    for n in range(1, m):
        c, b, a, p = m**2+n**2, 2*m*n, m**2-n**2, 2*m*(m+n)
        b, a = max(b, a), min(b, a)
        k = 1
        while k*p < 1000:
            counter[k*p].add((k*a, k*b, k*c))
            k += 1

print(max(counter.items(), key=lambda t: len(t[1])))
