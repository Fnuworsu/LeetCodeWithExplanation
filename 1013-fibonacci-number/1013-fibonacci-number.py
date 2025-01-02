class Solution:
    def fib(self, n: int) -> int:
        memo = {}

        if n == 0: return 0
        if n == 1: return 1

        if n in memo: return memo[n]

        memo[n] = self.fib(n-1) + self.fib(n-2)

        return memo[n]