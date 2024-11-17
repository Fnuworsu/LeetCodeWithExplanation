class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        res = ""

        i = j = 0

        while i < l1 or j < l2:
            if i < l1:
                res += word1[i]
                i += 1
            if j < l2:
                res += word2[j]
                j += 1

        return res            
        