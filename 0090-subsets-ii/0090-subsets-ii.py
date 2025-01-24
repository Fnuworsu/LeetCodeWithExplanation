class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        visited = set()

        def backtrack(i, path):
            nonlocal res

            if i == len(nums):
                if tuple(path[:]) not in visited:
                    res.append(path[:])
                    visited.add(tuple(path[:]))

                return
            
            path.append(nums[i])
            backtrack(i+1, path)

            path.pop()
            backtrack(i+1, path)
        
        backtrack(0, [])

        return res
        