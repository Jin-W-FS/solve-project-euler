from common import Factorize2

d = {}
for i in range(1, 21):
    f = Factorize2(i)
    for k, v in f.items():
        if d.get(k, 0) < v:
            d[k] = v

s = 1
for k, v in d.items():
    s *= k ** v
print(s)
