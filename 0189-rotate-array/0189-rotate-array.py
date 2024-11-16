class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [1,2,3,4,5,6,7]
        [1,2,3,4] [5,6,7]
        [7,2,3,4] [5,6,1]
        []
        """
        #----Brute force:

        res = deque(nums)

        while k > 0:
            res.appendleft(res.pop())
            k -= 1

        for i in range(len(nums)):
            nums[i] = res[i]  

            

        