class Solution:
    def replaceDigits(self, s: str) -> str:
        chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        idx = lambda c: ord(c) - ord('a')
        res = ""

        for i in range(len(s)):
            if i % 2:
                res += chars[idx(s[i-1]) + int(s[i])]
            else:
                res += s[i]
        
        return res