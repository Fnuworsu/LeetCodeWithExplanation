class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def back(i, path):
            nonlocal res

            if i == len(candidates) or sum(path) > target:
                return
            
            if sum(path) == target:
                res.append(path[:])
                return
            
            for j in range(i, len(candidates)):
                path.append(candidates[j])
                back(j, path)
                path.pop()
        
        back(0, [])

        return res
        