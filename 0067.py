s = open('data/p067_triangle.txt').read()
ll = [[int(x) for x in l.split()] for l in s.split('\n') if l]

for i in range(len(ll)-2, -1, -1):
    t, b = ll[i], ll[i+1]
    for j in range(len(t)):
        t[j] = t[j] + max(b[j], b[j+1])
