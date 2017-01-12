from heapq import heappush, heappop

mat = [[int(x) for x in l.split(',')] for l in open('data/p083_matrix.txt')]
N = len(mat)    # assert mat is square

inf = float('inf')

class Dijkstra:
    DIRS = ((1, 0), (0, 1), (0, -1), (-1, 0))
    
    def init(self, src, dst):
        self.src, self.dst = src, dst
        self.open = []   # heapqueue
        self.closed = set()
        
    def succs(self, x0, y0):
        for d in Dijkstra.DIRS:
            x, y = x0+d[0], y0+d[1]
            if 0 <= x < N and 0 <= y < N:
                yield x, y

    def update(self, c0, x0, y0):
        self.closed.add((x0, y0))
        for x, y in self.succs(x0, y0):
            if (x, y) in self.closed: continue
            heappush(self.open, (c0 + mat[x][y], x, y))

    def build(self):
        x, y = self.src
        c = mat[x][y]
        while (x, y) != self.dst:
            self.update(c, x, y)
            c, x, y = heappop(self.open)
        return c

d = Dijkstra()
d.init((0, 0), (N-1, N-1))
print(d.build())
