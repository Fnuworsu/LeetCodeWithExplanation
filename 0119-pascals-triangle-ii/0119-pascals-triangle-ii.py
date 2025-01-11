class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1],[1,1],[1,2,1]]

        if rowIndex < 3:
            return dp[rowIndex]
        idx = 3
        for i in range(3, rowIndex+1):
            res = [1 for _ in range(i+1)]
            for j in range(1, len(res)-1):
                res[j] = dp[i%idx-1][j-1] + dp[i%idx-1][~j]
            dp[-1] = res
            idx += 1

        return dp[-1]        