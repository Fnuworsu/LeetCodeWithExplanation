class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph)-1
        res = []

        def backtrack(path, node):
            if path[-1] == target:
                res.append(path[:])
                return

            for nb in graph[node]:
                path.append(nb)
                backtrack(path, nb)
                path.pop()

        backtrack([0], 0)

        return res            
        