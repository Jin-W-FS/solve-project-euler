from common import ProperDivisors

N = 10000
l = [0] * N
amicable  = []
for i in range(N):
    l[i] = sum(ProperDivisors(i))
    if l[i] < i and l[l[i]] == i:
        amicable.append((l[i], i))

print(amicable)
print(sum(x + y for x, y in amicable))
