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
                return True

        return False                                        

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(goal) != len(s):
            return False

        kmp = KMP(goal)
        return kmp.match(s * 2)    
        