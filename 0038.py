'''solve: 9abc * 2 = defgh which maximizes 9abc'''

def unduplicated(*nums):
    from common import digits
    from itertools import chain
    s = set()
    for d in chain.from_iterable(str(n) for n in nums):
        if d in s: return False
        s.add(d)
    return True

for n in range(9876, 9000, -1):
    if unduplicated(0, n, n*2):
        break
print(n, 2*n)
print(n, 2*n, sep='')

