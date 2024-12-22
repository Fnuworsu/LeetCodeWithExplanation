class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        rank = [1 for _ in range(n+1)]
        pars = [_ for _ in range(n+1)]

        def find(a):
            p = pars[a]

            while p != pars[p]:
                p = pars[p]

            return p  

        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False

            if rank[pa] > rank[pb]:
                rank[pa] += rank[pb]
                pars[pb] = pars[pa]
            else:
                rank[pb] += rank[pa]
                pars[pa] = pars[pb]    

            return True

        for a,b in edges:
            if not union(a,b):
                return [a,b]                  
        