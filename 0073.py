from math import ceil
from common import gcd

N = 12000

s = 0
for i in range(4, N+1):    
    for j in range(i//3+1, ceil(i/2)):
        s += (gcd(j, i) == 1)
print(s)
