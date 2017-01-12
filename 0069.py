from common import prim
from itertools import count

s = 1
for i in count():
    p = prim(i)
    n = s * p
    if n >= 1000000: break
    s = n

print(s)

