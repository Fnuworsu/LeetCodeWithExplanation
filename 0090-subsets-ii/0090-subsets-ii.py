class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        Set = set()

        def backtrack(stack, i):
            if i == len(nums):
                if tuple(stack[:]) not in Set:
                    res.append(stack[:])
                    Set.add(tuple(stack[:]))
                return

            #include
            stack.append(nums[i])
            backtrack(stack, i+1)

            #exclude
            stack.pop()
            backtrack(stack, i+1)

        backtrack([], 0)

        return res    



        