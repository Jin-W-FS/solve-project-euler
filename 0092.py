from common import digits

N = 10000000
cache = [None] * 600
cache[0] = False
cache[1] = False
cache[89] = True

def nextNum(n):
    return sum(v**2 for v in digits(n))

def check(n):
    if n < len(cache):
        if cache[n] is not None:
            return cache[n]
        else:
            rlt = cache[n] = check(nextNum(n))
            return rlt
    else:
        return check(nextNum(n))

print(sum(check(n) for n in range(1, N)))
