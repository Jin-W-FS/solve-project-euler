# mat = [[1, 2],[3, 4]]
mat = [[int(x) for x in l.split(',')] for l in open('data/p081_matrix.txt')]

inf = float('inf')
def elem(mat, i, j):
    if 0 <= i < len(mat) and 0 <= j < len(mat[0]):
        return mat[i][j]
    else:
        return inf

for i in range(len(mat)):
    for j in range(len(mat[0])):
        if i == j == 0: continue
        mat[i][j] += min(elem(mat, i-1, j), elem(mat, i, j-1))

print(mat[-1][-1])
