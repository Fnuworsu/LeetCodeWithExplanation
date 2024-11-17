class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force approach
        res = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in res:
                return [i, res[diff]]
            res[n] = i     
        