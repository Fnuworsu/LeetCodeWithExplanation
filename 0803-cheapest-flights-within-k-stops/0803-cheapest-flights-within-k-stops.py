import heapq
from collections import defaultdict
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Build the graph
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Priority queue for Dijkstra-like BFS: (cost, stops, node)
        pq = [(0, 0, src)]  # (cost, steps, node)
        
        # Distances: dist[node][steps] = min cost to reach `node` with `steps` stops
        dist = [[float('inf')] * (k + 2) for _ in range(n)]  # (k+1) stops are allowed, plus 1 for 0 stops.
        dist[src][0] = 0
        
        while pq:
            cost, steps, node = heapq.heappop(pq)

            # If we've reached the destination, return the cost
            if node == dst:
                return cost
            
            # If we've used more than `k` stops, we don't proceed further
            if steps > k:
                continue

            # Explore neighbors (u -> v) with current stop count
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                if new_cost < dist[neighbor][steps + 1]:
                    dist[neighbor][steps + 1] = new_cost
                    heapq.heappush(pq, (new_cost, steps + 1, neighbor))
        
        # If no path is found within `k` stops, return -1
        return -1
