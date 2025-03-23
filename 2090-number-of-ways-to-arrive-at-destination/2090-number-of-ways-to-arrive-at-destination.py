class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        graph = defaultdict(list)

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        #        dist,      path
        dist = defaultdict(lambda: [float("inf"), 0])
        dist[0][0] = 0
        dist[0][1] = 1
        pq = [(0, 0)]

        while pq:
            d, node = heapq.heappop(pq)
            
            if d > dist[node][0]:
                continue
            
            for nb,w in graph[node]:
                newD = d + w
                if newD < dist[nb][0]:
                    dist[nb] = [newD, dist[node][1]]
                    heapq.heappush(pq, (newD, nb))
                elif newD == dist[nb][0]:
                    dist[nb][1] += dist[node][1]
        print(dist)
        return dist[n-1][1] % MOD