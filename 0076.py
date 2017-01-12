from common import lru_cache

ITEMS = list(range(1, 100))

@lru_cache(maxsize=None)
def combWays(total, maxi=len(ITEMS)-1):
    if maxi == 0:
        # return (total % ITEMS[maxi] == 0)
        return 1
    return sum(combWays(total - ITEMS[maxi] * i, maxi - 1)
               for i in range(total//ITEMS[maxi], -1, -1))

print(combWays(100))

