class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        discoveryTime = [-1 for _ in range(n)]
        lowTime = [-1 for _ in range(n)]
        visited = [0 for _ in range(n)]
        timer = 0

        graph = defaultdict(list)

        for u,v in connections:
            graph[u].append(v)
            graph[v].append(u)

        res = []
        #parent = backedge
        def dfs(node, parent=-1):
            nonlocal timer

            discoveryTime[node] = timer
            lowTime[node] = timer
            visited[node] = 1
            timer += 1

            for nb in graph[node]:
                if nb == parent:
                    continue
                #nb already visited
                if visited[nb]:
                    lowTime[node] = min(lowTime[node], discoveryTime[nb])

                else:
                    dfs(nb, node)
                    lowTime[node] = min(lowTime[node], lowTime[nb])

                    if lowTime[nb] > discoveryTime[node]:
                        res.append([node,nb])
        
        for node in range(n):
            if not visited[node]:
                dfs(node)
        
        return res
        

        