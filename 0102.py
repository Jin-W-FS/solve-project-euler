

def sig(v):
    if v == 0:
        return 0
    elif v > 0:
        return 1
    else:
        return -1

def det(x1, y1, x2, y2):
    return (x1 * y2 - x2 * y1)

def triDir(x1, y1, x2, y2):
    return sig(det(x1, y1, x2, y2))

def containsOrigin(x0, y0, x1, y1, x2, y2):
    '''check if ABO, BCO, CAO in a same rotation direction'''
    return triDir(x0, y0, x1, y1) == triDir(x1, y1, x2, y2) == triDir(x2, y2, x0, y0)


c = 0
for line in open('data/p102_triangles.txt'):
    v = [int(s) for s in line.split(',')]
    c += containsOrigin(*v)
print(c)

