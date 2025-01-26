class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        even and odd
        a:1
        c: 4
        d: 2
        """
        hMap = defaultdict(int)

        for c in s: hMap[c] += 1

        odd = 0
        res = 0

        for v in hMap.values():
            if v % 2 == 1:
                odd = 1
                res += (v-1)
            else:
                res += v
        
        return res + odd


        