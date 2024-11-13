class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        diff = abs(l1 - l2)
        res = ""

        if l1 > l2:
            while diff > 0:
                l1 -= 1
                diff -= 1
        else:
            while diff > 0:
                l2 -= 1
                diff -= 1
        #l1 == l2

        for i in range(l1):
            res += word1[i]
            res += word2[i]

        if l1 < len(word1): res += word1[l1:]
        if l2 < len(word2): res += word2[l2:]    

        return res
                        
        