class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('-inf')
        minD = float('inf')

        for n in nums:
            minD = min(minD, abs(n))
        
        for n in nums:
            if abs(n) == minD:
                res = max(n, res)
        
        return res