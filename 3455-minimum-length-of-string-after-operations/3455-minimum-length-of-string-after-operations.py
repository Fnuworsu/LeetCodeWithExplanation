class Solution:
    def minimumLength(self, s: str) -> int:
        idx = lambda c: ord(c) - ord('a')

        freq = [0] * 26
        res = 0

        for c in s:
            i = idx(c)
            freq[i] += 1

            if freq[i] == 3:
                res += 2
                freq[i] = 1
        
        return len(s) - res

        