class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        totSum = (n * (n+1)) // 2
        currSum = sum(nums)

        return totSum - currSum