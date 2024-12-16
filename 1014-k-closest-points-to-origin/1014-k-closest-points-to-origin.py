class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []

        for x,y in points:
            d = x**2 + y**2
            minHeap.append([d, [x,y]])

        heapq.heapify(minHeap)
        res = []

        while k > 0:
            val = heapq.heappop(minHeap)
            res.append(val[1])
            k -= 1

        return res    
        