class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1 for _ in range(n)]
        pars = [x for x in range(n)]

        def find(a):
            p = pars[a]
            while p != pars[p]:
                p = pars[p]
            return p

        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                if rank[pa] > rank[pb]:
                    rank[pa] += rank[pb]
                    pars[pb] = pars[pa]
                else:
                    rank[pb] += rank[pa]
                    pars[pa] = pars[pb]

        graph = defaultdict(list)
        components = defaultdict(list)

        for a,b in edges:
            union(a,b)
            graph[a].append(b)
            graph[b].append(a)

        for node in range(n):
            components[find(node)].append(node)

        def isComplete(comp):
            nC, eC = len(comp), 0
            if not comp: return False
            for node in comp:
                eC += len(graph[node])
            eC //= 2

            return eC == (nC * (nC-1)) // 2               
    

        print(components)    
        res = 0

        for comp in components.values():
            if isComplete(comp):
                res += 1

        return res        

        