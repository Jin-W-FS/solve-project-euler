from common import lru_cache

def nextnum(n):
    if n <= 1: return 1
    q, r = divmod(n, 2)
    if r:
        return 3 * n + 1
    else:
        return q

@lru_cache(maxsize=None)
def seqlen(n):
    if n <= 1: return 0
    return 1 + seqlen(nextnum(n))

print(max((seqlen(i), i) for i in range(1000000)))
