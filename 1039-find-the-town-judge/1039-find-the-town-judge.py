class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inMap = defaultdict(int)
        outMap = defaultdict(int)

        for a, b in trust:
            outMap[a] += 1
            inMap[b] += 1

        for i in range(1, n+1):
            if outMap[i] == 0 and inMap[i] == n-1:
                return i

        return -1            
        