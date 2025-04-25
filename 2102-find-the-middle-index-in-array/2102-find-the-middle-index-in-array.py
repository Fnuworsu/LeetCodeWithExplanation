class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # 2 5 4 12 16
        if len(nums) == 1:
            return 0

        prefix = [nums[0]]
        
        for n in nums[1:]:
            prefix.append(prefix[-1] + n)
        
        
        for i in range(len(nums)):
            l = prefix[i-1] if i-1 >= 0 else 0
            r = prefix[-1] - prefix[i]

            print(l,r)

            if l == r:
                return i
        
        return -1