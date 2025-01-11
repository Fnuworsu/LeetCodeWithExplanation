class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[] for _ in range(numRows)]

        if numRows < 2:
            return [[1]]

        dp[0] = [1]
        dp[1] = [1,1]

        for i in range(2, numRows):
            res = [1 for _ in range(i+1)]
            for j in range(1,len(res)-1):
                res[j] = dp[i-1][j-1] + dp[i-1][-j-1]
            dp[i] = res

        return dp    

