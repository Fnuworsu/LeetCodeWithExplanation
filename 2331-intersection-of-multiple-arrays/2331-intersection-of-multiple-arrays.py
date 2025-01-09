class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        set1 = set(nums[0])

        for r in nums[1:]:
            set2 = set(r)
            set1 = set1.intersection(set2)

        res = list(set1) 
        res.sort()

        return res  
            


        