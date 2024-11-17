class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        res = ""

        i, j = 0, 0

        while i < l1 and j < l2:
            res += word1[i]
            res += word2[j]
            i += 1
            j += 1

        if i < l1: res += word1[i:]
        if j < l2: res += word2[j:] 

        return res   

        