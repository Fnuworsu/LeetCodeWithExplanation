class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges) + 1
        graph = defaultdict(set)
        
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = deque([node for node in range(1, n+1) if len(graph[node]) == 1])
        numNodes = n

        while numNodes > 2:
            numLeaves = len(leaves)
            numNodes -= numLeaves

            for _ in range(numLeaves):
                leafNode = leaves.popleft()
                for nb in graph[leafNode]:
                    graph[nb].remove(leafNode)
                    if len(graph[nb]) == 1:
                        leaves.append(nb)

        return leaves[0]                

        