class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [x for x in range(1, n+1)]
        res = []

        def backtrack(stack, i):
            if i == n: return 

            #include
            stack.append(nums[i])
            if len(stack) == k:
                res.append(stack[:])
            backtrack(stack, i+1)

            #exclude
            stack.pop()
            backtrack(stack, i+1)

        backtrack([], 0)

        return res        

        