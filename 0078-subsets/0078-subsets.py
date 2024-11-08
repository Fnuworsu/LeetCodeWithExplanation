class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(stack, i):
            if i == len(nums):
                res.append(stack[:])
                return
                
            #include
            stack.append(nums[i])
            backtrack(stack, i+1)

            #exclude
            stack.pop()
            backtrack(stack, i+1)

        backtrack([], 0)

        return res     
        