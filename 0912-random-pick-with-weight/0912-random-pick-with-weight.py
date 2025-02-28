import random as rd

class Solution:
    def __init__(self, w: List[int]):
        self.prefix = [w[0]]
        if len(w) == 1:
            return
        
        for n in w[1:]:
            self.prefix.append(self.prefix[-1] + n)

    def pickIndex(self) -> int:
        total = self.prefix[-1]
        target = total * rd.random()
        l, r = 0, len(self.prefix)-1

        while l <= r:
            mid = (l+r) // 2
            if target < self.prefix[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()