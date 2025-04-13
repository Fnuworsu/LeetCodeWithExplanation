class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        cache = set(nums)
        l = 1
        maxLen = 1

        for n in cache:
            if (n-1) in cache:
                continue
            
            x = n

            while x+1 in cache:
                x += 1
                l += 1
            
            maxLen = max(maxLen, l)
            l = 1
        
        return maxLen

