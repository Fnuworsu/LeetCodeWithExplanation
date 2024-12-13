class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)

        for k,v,w in edges:
            graph[k].append((v,w))
            graph[v].append((k,w))

        def shortestPath(start):
            res = 0
            minDist = {node : float("inf") for node in range(n)}
            minDist[start] = 0
            pq = [(0, start)]

            while pq:
                d, node = heapq.heappop(pq)

                if d > minDist[node]:
                    continue

                for nb, w in graph[node]:
                    dist = d + w
                    if dist < minDist[nb]:
                        minDist[nb] = dist
                        heapq.heappush(pq, (dist, nb))

                if d <= distanceThreshold:
                    res += 1

            return res                

        res = [(0, node) for node in range(n)]

        for node in range(n):  
            minD = shortestPath(node)
            res[node] = (minD, node)

        res.sort(key=lambda x:(x[0], -x[1]))  
        print(res)

        return res[0][1]              