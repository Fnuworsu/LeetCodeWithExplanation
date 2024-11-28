class Solution:
    def check(self, res, w1, w2):
        i, j = 0, 0

        while i < len(w1) and j < len(w2):
            if res[w1[i]] < res[w2[j]]:
                return True
            elif res[w1[i]] > res[w2[j]]:
                return False
            i += 1
            j += 1

        return len(w1) <= len(w2)   

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        res = {}

        for i, c in enumerate(order):
            res[c] = i

        for i in range(1, len(words)):
            if not self.check(res, words[i-1], words[i]):
                return False

        return True            
        