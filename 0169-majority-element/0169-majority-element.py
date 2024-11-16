# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         n = len(nums) // 2
#         res = defaultdict(int)

#         for n in nums:
#             res[n] += 1

#         for k, v in res.items():
#             if v > n:
#                 return k 


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = defaultdict(int)
        l  = len(nums) // 2

        for n in nums:
            res[n] += 1
        for k, v in res.items():
            
            if v > l:     
                return k
        