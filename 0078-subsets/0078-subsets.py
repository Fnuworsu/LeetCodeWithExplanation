class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # accumulator

        def backtrack(stack, i):
            # print(res)
            if i == len(nums):
                """
                After searching through the whole of nums 
                """
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
        