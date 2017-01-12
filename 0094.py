# a**2 + b**2 = c**2
# a = (c + 1) / 2 or (c - 1) / 2
# b**2 = c**2 - a**2 = (3c+1)(c-1)/4 or (3c-1)(c+1)/4
# let c = 2m+1, b**2 = (3m+2)m or (3m+1)(m+1) = (3n-2)n
# c <= (10**9 + 1) // 3 = 333,333,333,333, m = (c - 1) // 2 <= 166666666

def test1():
    def check(p):
        from math import sqrt
        sq = sqrt(p)
        return int(sq) == sq

    match = []
    for i in range(1, 166666666):
        p1, p2 = (3*i-2)*i, (3*i+2)*i, 
        if check(p1): match.append((2*i-1, i-1))
        if check(p2): match.append((2*i+1, i+1))
    match.pop(0)
    s = 2*sum(x+y for x, y in match)
    print(s)    # 5479171588

# a, b, c = m**2-n**2, 4*m*n, m**2+n**2, (k**2 == 1) m > n
# m**2+n**2 = 2*(m**2-n**2) +- 1 or m**2+n**2 = 8*m*n +- 1
# 3*n**2 - m**2 = +-1 or m**2-8*m*n+n**2 = +-1

