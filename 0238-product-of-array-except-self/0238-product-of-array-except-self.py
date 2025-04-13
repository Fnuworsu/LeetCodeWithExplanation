class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1] * n
        r = [1] * n

        for i in range(1, n):
            l[i] = nums[i-1] * l[i-1]
        
        for i in range(n-2, -1, -1):
            r[i] = nums[i+1] * r[i+1]
        print(l)
        print(r)
        return [x*y for x,y in zip(l,r)]