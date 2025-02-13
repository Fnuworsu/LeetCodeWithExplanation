import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        """
        add min(x,y) * 2 + max(x,y)
        nums[0] >= k
        """
        heapq.heapify(nums)
        ops = 0

        while len(nums) >= 2:
            if nums[0] >= k:
                return ops

            x,y = heapq.heappop(nums), heapq.heappop(nums)
            heapq.heappush(nums, 2 * min(x,y) + max(x,y))
            ops += 1
        
        return ops

            
        

        