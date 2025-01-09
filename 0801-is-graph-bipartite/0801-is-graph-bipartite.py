class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [0 for _ in range(len(graph))]
        
        def bipart(node):
            if color[node]:
                return True

            q = deque([node])
            color[node] = 1

            while q:
                curr = q.popleft()
                for nb in graph[curr]:
                    if color[curr] == color[nb]:
                        return False
                    elif not color[nb]:
                        q.append(nb)
                        color[nb] = -1 * color[curr]

            return True

        for node in range(len(graph)):
            if not bipart(node):
                return False

        return True                           
        