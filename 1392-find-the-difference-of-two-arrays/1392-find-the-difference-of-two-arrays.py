class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res =[[],[]]

        set1 = set(nums2)
        set2 = set(nums1)

        for n in nums1:
            if n not in set1: 
                res[0].append(n)
                set1.add(n)

        for n in nums2:
            if n not in set2:
                res[1].append(n)
                set2.add(n)

        return res           

        