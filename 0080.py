from math import sqrt

def sqrti(y):
    x, dx = round(sqrt(y)), 1
    while dx:
        dx = (y - x**2)//(2*x)
        x += dx
    return x

def sum100digits(n):
    return sum(int(x) for x in str(n)[:100])

def check(x):
    if int(sqrt(x))**2 == x: return 0
    return sum100digits(sqrti(x*10**200))

print(sum(check(x) for x in range(1, 101)))
