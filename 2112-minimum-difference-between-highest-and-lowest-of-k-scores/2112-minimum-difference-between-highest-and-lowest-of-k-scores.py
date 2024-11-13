class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        s = 0
        res = float('inf')

        for f in range(len(nums)):
            if (f - s + 1) == k:
                minN, maxN = nums[s], nums[f]
                res = min(res, maxN - minN)
                s += 1

        return res        
        