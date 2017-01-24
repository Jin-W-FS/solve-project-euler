from common import Factorize

d = {}
for i in range(1, 21):
    f = Factorize(i)
    for k, v in f.items():
        if d.get(k, 0) < v:
            d[k] = v

s = 1
for k, v in d.items():
    s *= k ** v
print(s)
