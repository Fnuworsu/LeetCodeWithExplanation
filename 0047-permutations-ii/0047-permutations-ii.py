class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [0 for _ in nums]

        def backtrack(path, used, acc):
            nonlocal res
            if len(path) == len(nums):
                if tuple(path) not in acc:
                    res.append(path[:])
                acc.add(tuple(path)) 
                return

            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = 1
                
                backtrack(path, used, acc)
                path.pop()
                used[i] = 0

        backtrack([], used, set())

        return res                
        