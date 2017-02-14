from common import count

W = []   # W[n][m]

class Ways(list):
    def __init__(self, n):
        super().__init__([0]*n)
        self.n = n
    def __getitem__(self, m):
        if self.n == 0: return 1
        if m <= 0: return 0
        if m > self.n: return self[self.n]
        return super().__getitem__(m-1)
    def __setitem__(self, m, v):
        super().__setitem__(m-1, v)

def buildLine(n):
    '''build W[n], assume W[:n] was built'''
    Wn = Ways(n)
    W.append(Wn)
    for m in range(1, n+1):
        Wn[m] = W[n-m][m] + Wn[m-1]

for n in count():
    buildLine(n)
    if W[n][n] % 1000000 == 0: break
print(n)


