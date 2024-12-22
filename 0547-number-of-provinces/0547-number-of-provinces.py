class UnionFind:
    def __init__(self,n):
        self.rank = [1 for _ in range(n)]
        self.pars = [x for x in range(n)]

    def find(self,a):
        p = self.pars[a]
        while p != self.pars[p]:
            p = self.pars[p]
        return p

    def union(self,a,b):
        pa, pb = self.find(a), self.find(b)

        if pa == pb:
            return False #cycle

        if self.rank[pa] > self.rank[pb]:
            self.rank[pa] += self.rank[pb]
            self.pars[pb] = self.pars[pa]
        else:
            self.rank[pb] += self.rank[pa]
            self.pars[pa] = self.pars[pb]

        return True

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])
        uf = UnionFind(rows)
        components = rows

        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1 and uf.union(r,c):
                    components -= 1

        return components            
       
        