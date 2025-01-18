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
                return not (i-j)
        
        return False

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        #Using string matching
        kmp = KMP(searchWord)

        res = float('inf')
        i = 1

        for word in sentence.split():
            if kmp.match(word):
                res = min(res, i)
            i += 1

        return res if res != float('inf') else - 1
        