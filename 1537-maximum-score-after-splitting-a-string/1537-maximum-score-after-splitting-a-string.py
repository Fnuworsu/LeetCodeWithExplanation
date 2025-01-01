class Solution:
    def maxScore(self, s: str) -> int:
        res = 0

        for i in range(1, len(s)):
            print(s[:i], s[i:])
            opt1 = s[:i].count('0')
            opt2 = s[i:].count('1')
            print(opt1 + opt2)
            
            res = max(res, opt1 + opt2)

        return res    
        