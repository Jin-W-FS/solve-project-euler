from common import digits

factorials = [1] * 10
for i in range(1, 10):
   factorials[i] = factorials[i-1] * i
   
# for n in range(9): print(n * factorials[9], 10**n-1)

N = 9
l, n, s = [0, 1], 10, 2

def sfd(l):
    return sum(factorials[x] for x in l)

def calcNext():
    global l, n, s
    n += 1
    c = 1
    for i, d in enumerate(l):
        if c:
            s -= factorials[d]
            if d == 9:
                l[i] = 0
                c = 1
            else:
                l[i] += 1
                c = 0
            s += factorials[l[i]]
        else:
            break
    if c:
        l.append(c)
        s += factorials[c]

nums = []
while len(l) < N:
    if n == s:
        print(n)
        nums.append(n)
    calcNext()

print(nums, sum(nums))
# [145, 40585] 40730
