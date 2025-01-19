class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        numSet = set()

        for u,v in edges:
            numSet.add(u)
            numSet.add(v)

            graph[u].append(v)
            graph[v].append(u)
        
        numNodes = len(numSet)-1

        for k,v in graph.items():
            if len(v) == numNodes:
                return k


        