class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        if 0 <= x < 10:
            return True

        def solve(n=x):
            res = 0

            while n > 0:
                rem = n % 10
                res = res * 10 + rem
                n //= 10

            return res    

        res = solve()
        # print(x, res)

        return res == x        

        