class KMP:
    def __init__(self, pattern):
        self.pattern = pattern
        self.lps = [0] * len(pattern)

        i = 1
        j = 0

        while i < len(pattern):
            if pattern[i] == pattern[j]:
                self.lps[i] = j + 1
                i += 1
                j += 1
            elif j == 0:
                self.lps[i] = 0
                i += 1
            else:
                j = self.lps[j - 1]
    
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
                return True
        
        return False

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        words = [word * i for i in range(1, len(sequence) // len(word) + 1)]
        k = len(word)
        # print(words)
        res = 0

        for w in words:
            kmp = KMP(w)
            if kmp.match(sequence):
                res = max(res, len(w))

        return res // k
        