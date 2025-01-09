class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        return n > 0 and n & (n-1) == 0 and n % 2 == 0
        