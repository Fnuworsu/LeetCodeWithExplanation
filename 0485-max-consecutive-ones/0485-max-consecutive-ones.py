class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr, maxN = 0, 0

        for n in nums:
            if n == 1:
                curr += 1
            else:
                maxN = max(maxN, curr)
                curr = 0
        
        return max(curr, maxN)
        