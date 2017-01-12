
def digits(n):
    while n:
        n, r = divmod(n, 10)
        yield r

def choosen(n):
    for x in range(10**(n-1), 10**n):
        s = set(digits(x))
        if 0 in s or len(s) != n: continue
        yield x, s

s = set()
for a in range(2, 10):
    for b, sb in choosen(4):
        if a in sb: continue
        c = a * b
        if not 1000 <= c < 10000: continue
        sc = set(digits(c))
        if 0 in sc or len(sc) != 4: continue
        if len({a} | sb | sc) != 9: continue
        print(a, '*', b, '=', c)
        s.add(c)

for a, sa in choosen(2):
    for b, sb in choosen(3):
        if sa & sb: continue
        c = a * b
        if not 1000 <= c < 10000: continue
        sc = set(digits(c))
        if 0 in sc or len(sc) != 4: continue
        if len(sa | sb | sc) != 9: continue
        print(a, '*', b, '=', c)
        s.add(c)

print(sum(s))

