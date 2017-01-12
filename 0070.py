from common import totients_lt, digits

N = 10**7
totients = totients_lt(N)

l = [n for n in range(2, N)
    if sorted(digits(n)) == sorted(digits(totients[n]))]

print(min(l, key=lambda n: n / totients[n]))
