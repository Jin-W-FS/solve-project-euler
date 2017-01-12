from common import ProperDivisors

def isAbundant(x):
    return sum(ProperDivisors(x)) > x

N = 28124
abundants = list(filter(isAbundant, range(1, N)))
fs = list(range(N))
for x in abundants:
    for y in abundants:
        s = x + y
        if s < len(fs):
            fs[s] = False
        else:
            break
print(sum(fs))

