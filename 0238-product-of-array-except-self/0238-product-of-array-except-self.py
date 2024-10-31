import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1
        for i, n in enumerate(nums):
            res[i] = prefix
            prefix *= n

        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            res[i] *= suffix
            suffix *= n

        return res        
        