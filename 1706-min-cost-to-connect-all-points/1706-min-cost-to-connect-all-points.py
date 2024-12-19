class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        [3,10]
        [0,0]
        [2,2]
        """
        #Prim's
        edges = []
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                w = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i,j,w])

        print(edges)

        graph = defaultdict(list)

        for u,v,w in edges:
            graph[u].append((v,w))
            graph[v].append((u,w))

        pq = [(0, 0)] #w, node
        visited = set()
        cost = 0

        while pq:
            c, node = heapq.heappop(pq)

            if node in visited:
                continue
            visited.add(node)
            cost += c

            for nb,w in graph[node]:
                heapq.heappush(pq, (w,nb))    

        return cost                    
        