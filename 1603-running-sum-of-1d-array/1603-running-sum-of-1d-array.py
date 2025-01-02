class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]

        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        res = []

        for i in range(len(nums)):
            res.append(prefix[i])    
        
        return res