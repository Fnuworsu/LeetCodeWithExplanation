class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        [3,2,2,3] val = 3
        [-1,2,2,-1]
        """
        j = 0

        for i in range(len(nums)):
            if nums[i] == val:
                continue
            else:
                nums[j] = nums[i]
                j += 1

        return j            

        