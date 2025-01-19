class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        1.shortest path to all nodes
        2.earliest time is max shortest(reaches all nodes)     
        3. start node = k   
        """
        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        dist = {node:float('inf') for node in range(1,n+1)}
        dist[k] = 0

        pq = [(0,k)] #d,node

        while pq:
            d, node = heapq.heappop(pq)

            if d > dist[node]:
                continue
            
            for nb,w in graph[node]:
                newDist = w + d
                if newDist < dist[nb]:
                    dist[nb] = newDist
                    heapq.heappush(pq, (newDist, nb))
        
        res = -1
        print(dist.values())
        for v in dist.values():
            res = max(res, v)
        
        return res if res != float('inf') else -1