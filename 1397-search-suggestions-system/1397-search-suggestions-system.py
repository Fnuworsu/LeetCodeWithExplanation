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
                return (i-j) == 0
        
        return False

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        res = []
        pattern = ""
        products.sort()

        for c in searchWord:
            pattern += c
            acc = []
            kmp = KMP(pattern)

            for p in products:
                if kmp.match(p):
                    acc.append(p)

            if len(acc) > 3:
                res.append(acc[:3])
            else:
                res.append(acc)
        
        return res
            
        
        