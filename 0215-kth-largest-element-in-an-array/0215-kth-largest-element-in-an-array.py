class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        heap = [1,2,3,4,5,6]
        [5,6]
        [5]
        """
        heapify(nums)

        while len(nums) > k:
            heappop(nums)

        return heappop(nums)    