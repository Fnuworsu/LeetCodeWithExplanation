class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in numSet:
                l = 0
                while (n+l) in numSet:
                    l += 1
                longest = max(l, longest)

        return longest            
        