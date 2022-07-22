# Test UnionFind file is tests/test_union_find.py.

class UnionFind:
    def __init__(self, N):
        self.p = [-1 for i in range(N+1)]

    def find(self, x):
        if self.p[x] < 0:
            return x
        else:
            self.p[x] = self.find(self.p[x])
            return self.p[x]

    def unite(self, x, y):
        x,y = self.find(x), self.find(y)
        if x == y:
            return
        if self.size(x) < self.size(y):
            self.p[x] += self.p[y]
            self.p[y] = x
        else:
            self.p[y] += self.p[x]
            self.p[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def size(self, x):
        x = self.find(x)
        return -self.p[x]
