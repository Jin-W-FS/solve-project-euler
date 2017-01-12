# from itertools import count
# from common import prim
# s = 0
# for i in count():
    # p = prim(i)
    # if p >= 2000000: break
    # s += p
# print(s)

from common import prims_lt
print(sum(prims_lt(2000000)))
