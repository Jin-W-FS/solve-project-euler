
def Arranges(base):
    def ArrangeInc(l):
        c = 1
        for j in range(len(l)):
            idx, thd = -1-j, j+1
            l[idx] += c; c = 0
            if l[idx] >= thd:
                l[idx] -= thd; c = 1
            if c == 0:
                break
        return c
    def SwitchElemsLitera(l, base):
        base = list(base)
        return [base.pop(d) for d in l]
    base = list(base)
    l = [0] * len(base)
    c = 0
    while not c:
        yield SwitchElemsLitera(l, base)
        c = ArrangeInc(l)

def cmbint(l):
    r = 0
    for d in l:
        r = r * 10 + d
    return r

s = set()
for l in Arranges(range(1, 10)):
    a, b, c = l[0], cmbint(l[1:5]), cmbint(l[5:9])
    if a * b == c:
        print(a, '*', b, '=', c)
        s.add(c)
    a, b, c = cmbint(l[0:2]), cmbint(l[2:5]), cmbint(l[5:9])
    if a * b == c:
        print(a, '*', b, '=', c)
        s.add(c)
print(sum(s))

