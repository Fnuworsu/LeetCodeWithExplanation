class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n, rows, cols = len(isConnected), len(isConnected), len(isConnected[0])
        
        rank = [1 for _ in range(n)]
        pars = [x for x in range(n)]

        def find(a):
            p = pars[a]
            while p != pars[p]:
                p = pars[p]
            return p

        def union(a,b):
            pa, pb = find(a), find(b)

            if pa == pb:
                return False

            if rank[pa] > rank[pb]:
                rank[pa] += rank[pb]
                pars[pb] = pars[pa]
            else:
                rank[pb] += rank[pa]
                pars[pa] = pars[pb]

            return True

        graph = defaultdict(list)
        components = n

        for r in range(rows):
            for c in range(cols):
                if isConnected[r][c] == 1 and union(r,c):
                    components -= 1                       
        
        return components