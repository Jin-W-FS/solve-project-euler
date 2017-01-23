from common import Prims, prims_lt

M = 1000*1000
Prims.rebase(prims_lt(M))

N = len(Prims.lst)
sums = [0] * (N + 1)    # sums[i] = sum(Prims[:i]), sums[j] - sums[i] = sum(Prims[i:j])
for i in range(N): sums[i+1] = sums[i] + Prims[i]

md, mn, mi = 0, 0, 0
for j in range(N+1):
    for i in reversed(range(j - md)):
        n = sums[j] - sums[i]
        if n > M: break
        if n not in Prims: continue
        d = j - i
        if d > md: md, mn, mi = d, n, i

print(md, mn, mi)
