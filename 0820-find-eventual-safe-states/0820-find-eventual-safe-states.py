class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        """
        0 -> 1,2
        1 -> 2, 3
        2 -> 5
        3 -> 0
        4 -> 5
        5 -> 
        6 -> 
        []
        """
        visited, visiting = set(), set()
        acc = []

        def dfs(node):
            nonlocal acc

            if node in visited:
                return True
            if node in visiting:
                return False
            
            visiting.add(node)

            for nb in graph[node]:
                if not dfs(nb):
                    return False
            
            visiting.remove(node)
            visited.add(node)
            acc.append(node)
            return True
        
        for node in range(len(graph)):
            dfs(node)
        
        return sorted(acc)
        