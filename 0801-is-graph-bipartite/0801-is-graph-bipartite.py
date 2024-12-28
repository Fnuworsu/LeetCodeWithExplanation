class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        """
        take node color node blue, children red
        if color of node and children are the same, return false
        bfs
        """
        color = [0 for _ in range(len(graph))]

        def bfs(node):
            if color[node]:
                return True

            q = deque([node])
            color[node] = -1 #blue

            while q:
                node = q.popleft()

                for nb in graph[node]:
                    if color[node] == color[nb]:
                        return False
                    elif not color[nb]:
                        q.append(nb)
                        color[nb] = -1 * color[node]

            return True

        for node in range(len(graph)):
            if not bfs(node):
                return False  

        return True                    


    