
pow5 = [ x**5 for x in range(10) ]

def check(n):
    s = 0
    y = n
    while y:
        y, x = divmod(y, 10)
        s += pow5[x]
    return s == n

l = list(filter(check, range(2, 10**6)))
print(l, sum(l))
