class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        """
        NB: we only can have a MHT if number of nodes >= 2
        1.MHT has 1 center(for even nodes) or 2 centers(for odd nodes)
        2.Condition is while nodes with one degree are > 2
        3.remove one degree nodes from nb, and delete from the graph afterwards
        """
        if n == 1:
            return [0]

        graph = defaultdict(set)

        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        leaves = deque([node for node in range(n+1) if len(graph[node]) == 1])
        numNodes = n

        while numNodes > 2:
            leafCount = len(leaves)
            
            for _ in range(leafCount):
                leafNode = leaves.popleft()
                
                for nb in graph[leafNode]:
                    graph[nb].remove(leafNode)
                    if len(graph[nb]) == 1:
                        leaves.append(nb)
                
                del graph[leafNode]
            
            numNodes -= leafCount
        
        return list(leaves)
        