class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for a,b in edges:
            graph[a].add(b)
            graph[b].add(a)

        leaves = deque([node for node in range(n) if len(graph[node]) == 1])
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

                graph[leafNode] = [] 

        return list(leaves)                       
        