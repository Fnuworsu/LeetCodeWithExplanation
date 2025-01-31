class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hashMap = {0:0, 1:0, 2:0}

        for n in nums:
            hashMap[n] += 1
        
        i = 0

        for k,v in hashMap.items():
            for j in range(i, i+v):
                nums[j] = k
            i += v
        