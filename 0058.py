from common import Prims, prims_lt, isPrim2
Prims.rebase(prims_lt(1000000))
# print("build complete")

side, last, nnum, nprim = 1, 1, 1, 0
while True:
    side += 2
    newer = [last + (side-1) * x for x in range(1, 5)]
    last = newer[-1]
    nnum += 4
    nprim += sum(isPrim2(p) for p in newer[:-1]) # newer[-1] is always side**2
    if nprim / nnum < 0.1: break
    # print(side, nprim / nnum)
print(side)
