from common import palindromics

def check2(v):
    s = format(v, 'b')
    for i in range(len(s)//2):
        if s[i] != s[-i-1]: return False
    return True


s = 0
for l in range(1, 7):
    for n in palindromics(l):
        if check2(n):
            print(n, bin(n))
            s += n
print(s)
