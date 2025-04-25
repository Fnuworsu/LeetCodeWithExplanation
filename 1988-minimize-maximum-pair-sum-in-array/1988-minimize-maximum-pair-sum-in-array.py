class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        """
        [3,5,2,3]
        [2,3]
        [3,5]

        """
        nums.sort()
        n = len(nums)
        res = float('-inf')

        for i in range(n//2):
            res = max(res, nums[i] + nums[~i])
        
        return res