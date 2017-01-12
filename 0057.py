

n, d = 3, 2
s = 0
for i in range(1000):
    if len(str(n)) > len(str(d)): s += 1
    n, d = n + 2 * d, n + d
print(s)
