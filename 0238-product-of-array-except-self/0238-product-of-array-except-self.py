class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Using 1-D recurrence relation
        Notes:
        """
        n = len(nums)
        l, r = [1] * n, [1] * n

        for i in range(1, n):
            l[i] = nums[i-1] * l[i-1]
        
        for i in range(n-2, -1, -1):
            r[i] = nums[i+1] * r[i + 1]

        return [r[i] * l[i] for i in range(len(nums))]    
        