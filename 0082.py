from heapq import heappush, heappop

mat = [[int(x) for x in l.split(',')] for l in open('data/p082_matrix.txt')]
N = len(mat)    # assert mat is square

inf = float('inf')

class Dijkstra:
    DIRS = ((0, 1), (-1, 0), (1, 0))

    def init(self, src, dst):
        self.src, self.dst = set(src), set(dst)
        self.open = []   # heapqueue
        self.closed = set()
        
    def succs(self, x0, y0):
        for d in Dijkstra.DIRS:
            x, y = x0+d[0], y0+d[1]
            if 0 <= x < N and 0 <= y < N:
                yield x, y

    def update(self, c0, x0, y0):
        if (x0, y0) in self.closed: return
        self.closed.add((x0, y0))
        for x, y in self.succs(x0, y0):
            if (x, y) in self.closed: continue
            heappush(self.open, (c0 + mat[x][y], x, y))

    def build(self):
        for x, y in self.src:
            heappush(self.open, (mat[x][y], x, y))
        c, x, y = heappop(self.open)
        while (x, y) not in self.dst:
            self.update(c, x, y)
            c, x, y = heappop(self.open)
        return c

d = Dijkstra()
d.init(((i, 0) for i in range(N)), ((i, N-1) for i in range(N)))
print(d.build())
