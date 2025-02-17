class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openN, closeN, path):
            nonlocal res
            #base case
            if openN == closeN == n:
                res.append("".join(path[:]))
                return
            
            if openN < n:
                path.append('(')
                backtrack(openN+1, closeN, path)
                path.pop()
            
            if closeN < openN:
                path.append(')')
                backtrack(openN, closeN+1, path)
                path.pop()

        backtrack(0,0,[])

        return res

            
        