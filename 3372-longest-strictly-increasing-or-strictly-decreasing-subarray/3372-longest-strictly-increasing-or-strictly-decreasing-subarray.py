class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        """
        1 4 3 3 2
          
        """
        inc, dec = 1, 1
        maxLen = 0

        for i in range(1, len(nums)):
            x, y = nums[i-1], nums[i]
            if x < y:
                inc += 1
                maxLen = max(maxLen, dec)
                dec = 1
            elif x > y:
                maxLen = max(maxLen, inc)
                inc = 1
                dec += 1
            else:
                maxLen = max(maxLen, dec, inc)
                inc = 1
                dec = 1
            # print(x,y, inc)
            # print(x,y, dec)
            # print()
        return max(maxLen, dec, inc)


        