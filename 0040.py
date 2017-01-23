from common import count

def genChampernowne():
    for n in count():
        for s in str(n):
            yield s

m = 1
h = 1
for c, v in enumerate(genChampernowne()):
    if c == h:
        m *= int(v)
        if h == 1000000: break
        h *= 10
print(m)
