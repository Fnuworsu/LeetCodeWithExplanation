class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        resMap = defaultdict(int)  

        for c in s:
            resMap[c] += 1

        res = 0

        for v in resMap.values():
            res += (v % 2)

        return res <= k          
        