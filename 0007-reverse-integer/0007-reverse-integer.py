class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)

        def rev(n):
            res = 0

            while n > 0:
                acc = n % 10
                res += acc
                res *= 10

                n //= 10
            return res//10
        
        ans = rev(num)
        if x < 0:
            ans = -1 * ans
        
        if ans < -2**31 or ans > (2**31 - 1):
            return 0

        return ans
        