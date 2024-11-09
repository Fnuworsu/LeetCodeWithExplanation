class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        2 2 2 2
        2 2 2
        2 2 2 3
        """
        res = []
        
        def backtrack(stack, nums, i):
            # print(stack)
            if i == len(nums): return

            if sum(stack) > target: return

            if sum(stack) == target:
                res.append(stack[:])
                return
            
            #include
            stack.append(nums[i])
            backtrack(stack, nums, i)

            #exlude
            stack.pop()
            backtrack(stack, nums, i+1)

        backtrack([], candidates, 0)

        return res    

        