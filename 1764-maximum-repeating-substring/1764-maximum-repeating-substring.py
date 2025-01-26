class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        pattern = word
        res = 0

        while pattern in sequence:
            res += 1
            pattern += word
        
        return res
        