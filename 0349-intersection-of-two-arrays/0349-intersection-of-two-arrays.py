class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        Set = set(nums1)
        res = []

        for n in nums2:
            if n in Set:
                res.append(n)
                Set.remove(n)
        
        return res
