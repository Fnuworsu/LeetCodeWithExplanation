class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        """
        0 => n-1
        no cycle 
        e = [u,v] u -> v (u > v)
        0, 1, 2, 3
        (0,2) (1,3) (1,2)
        """
        graph = defaultdict(list)
        indegree = [0 for _ in range(n)]

        for u,v in edges:
            graph[u].append(v)
            indegree[v] += 1
        
        acc = []

        for i,n in enumerate(indegree):
            if not n:
                acc.append(i)
        
        if len(acc) > 1:
            return -1
        
        return acc[0]
        