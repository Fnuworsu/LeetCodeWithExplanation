class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        #RK
        pattern = s
        s = s*2
        haystack = "".join([s[i] for i in range(1, len(s)-1)])

        base = 31
        mod = 10 ** 9 + 7
        asci = lambda c: ord(c) - ord("a") + 1
        power = [1] * max(len(haystack), len(pattern))

        pHash = 0
        sHash = [0] * (len(haystack) + 1)

        for i in range(1, len(power)):
            power[i] = (power[i-1] * base) % mod
        
        for i in range(len(pattern)):
            pHash = (pHash + asci(pattern[i]) * power[i]) % mod
        
        for i in range(len(haystack)):
            sHash[i+1] = (sHash[i] + asci(haystack[i]) * power[i]) % mod
        
        matches = []

        for i in range(len(haystack) - len(pattern) + 1):
            currHash = (sHash[i+len(pattern)] + mod - sHash[i]) % mod

            if currHash == (pHash * power[i]) % mod:
                return True
        
        return False
        