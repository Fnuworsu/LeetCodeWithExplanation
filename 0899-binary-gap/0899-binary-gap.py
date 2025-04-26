class Solution:
    def binaryGap(self, n: int) -> int:
        binary = deque([])

        while n > 0:
            binary.appendleft(n & 1)
            n >>= 1
        
        l = 0
        res = 0
        
        for r in range(1, len(binary)):
            x = binary[r]
            if x == 1:
                res = max(res, r - l )
                l = r
        
        return res
        