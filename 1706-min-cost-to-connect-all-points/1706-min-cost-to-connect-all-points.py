class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        [3,10]
        [0,0]
        [2,2]
        """
        #kruskal
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i,j,w])

        n = len(points)
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

        edges.sort(key=lambda x:x[-1])  
        cost = 0
        nE = 0 #num of edges   

        for u,v,w in edges:
            if union(u,v):
                cost += w
                nE += 1
        # print(nE, n-1)

        return cost                            
        