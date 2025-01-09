class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = [0] * len(pattern)

        j = 0
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                self.lps[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                self.lps[i] = 0
                i += 1
            else:
                j = self.lps[j-1]

    def match(self, haystack):
        i = 0
        j = 0

        while i < len(haystack):
            if haystack[i] == self.pattern[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = self.lps[j-1]
            if j == len(self.pattern):
                return [True, abs(i-j)]

        return [False,-1]                                        

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        #using kmp
        res = 0

        for w in words:
            if len(w) < len(pref):
                continue
            if w[0] != pref[0]:
                continue    

            kmp = KMP(pref)
            acc = kmp.match(w)
            if acc[0] and acc[1] == 0: res += 1

        return res        