class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        a = 1
        b = 1
        c = 4
        d = 2
        """
        freq = Counter(s)
        even = 0
        odd = 0

        for v in freq.values():
            if not v % 2:
                even += v
            else:
                odd = 1
                even += (v-1)
        
        return odd + even
        