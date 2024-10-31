#using top-down(no memo)
"""class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        return self.fib(n-1) + self.fib(n-2) """

#using top-down(memo)
"""class Solution:
    def fib(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1

        memo = {}

        if n-1 not in memo:
            memo[n-1] = self.fib(n-1)
        if n-2 not in memo:
            memo[n-2] = self.fib(n-2)

        return memo[n-1] + memo[n-2]   """      

#using bottom-up(dp)
class Solution:
    def fib(self, n: int) -> int:   
        if n == 0: return 0
        
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]        
