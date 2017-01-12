lst = []
for d in range(1, 1000001):
    if d % 7 == 0: continue
    n = int(3 / 7 * d)
    lst.append((3/7-n/d, n, d))
    
print(min(lst))
