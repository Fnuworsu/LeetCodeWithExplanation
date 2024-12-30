class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []

        let = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        k = len(digits)
        res = []

        def backtrack(i, path):
            #base case
            if len(path) == k:
                # print("".join(path[:]))
                res.append("".join(path[:]))
                return

            for c in let[digits[i]]:
                path.append(c)
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])

        return res            