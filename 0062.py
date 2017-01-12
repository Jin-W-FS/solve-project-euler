from itertools import count

def base(n):
    v = 0
    for d in sorted(str(n), reverse=True):
        v = v * 10 + int(d)
    return v


d = {}
for i in count():
    n = i ** 3
    b = base(n)
    if not b in d:
        d[b] = [i]
    else:
        d[b].append(i)
        if len(d[b]) == 5: break
print(d[b])
