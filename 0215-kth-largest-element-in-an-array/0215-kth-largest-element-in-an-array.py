class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        res = -1

        while k != 0:
            res = heapq.heappop(heap)
            k -= 1

        return -res    
        