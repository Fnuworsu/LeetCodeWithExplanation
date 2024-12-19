class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0

        for n in nums:
            curr = n + max(curr, 0)
            res = max(res, curr)

        return res    
        