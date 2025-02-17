class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def isIn(arr, numSet):
            res = 0

            for n in arr:
                if n in numSet: res += 1
            
            return res
        
        numSet1, numSet2 = set(nums1), set(nums2)

        return [isIn(nums1, numSet2), isIn(nums2, numSet1)]
        