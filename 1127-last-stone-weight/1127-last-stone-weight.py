class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        x <= y
        1. if x == y: kill both
        2. else: x is destroyed y = y-x
        """
        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)

            if x == y:
                continue
            else:
                y = y - x
                heapq.heappush(heap, -y)

        if heap:
            return -heapq.heappop(heap)

        return 0            
         