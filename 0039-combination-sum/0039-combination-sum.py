class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(stack, i):
            # print(res, " =>", stack)
            if i == len(candidates) or sum(stack) > target:
                return

            if sum(stack) == target:
                res.append(stack[:])
                return

            #include
            stack.append(candidates[i])
            backtrack(stack, i)

            #exclude
            stack.pop()
            backtrack(stack, i+1)

        backtrack([], 0)    

        return res