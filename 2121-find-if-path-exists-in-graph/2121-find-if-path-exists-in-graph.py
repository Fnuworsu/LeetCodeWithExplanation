class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        dfs
        """
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def pathExist(graph, start, end):
            if start == end:
                return True

            visited.add(start)

            for nb in graph[start]:
                if nb not in visited:
                    if pathExist(graph, nb, end):
                        return True

            return False

        return pathExist(graph, source, destination)                        