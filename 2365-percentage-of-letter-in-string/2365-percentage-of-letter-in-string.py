class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        n = len(s)
        resMap = defaultdict(int)

        for c in s:
            resMap[c] += 1

        res = (resMap[letter] / n) * 100
        # print(res)

        return int(res)   

        