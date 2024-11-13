class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l1, l2 = len(word1), len(word2)
        diff = abs(l1 - l2)
        res = ""

        if l1 > l2:
            l1 -= diff
        else:
            l2 -= diff
        #l1 == l2

        for i in range(l1):
            res += word1[i]
            res += word2[i]

        if l1 < len(word1): res += word1[l1:]
        if l2 < len(word2): res += word2[l2:]    

        return res
                        
        