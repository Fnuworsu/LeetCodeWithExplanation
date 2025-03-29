class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        k = b/h
        [3,6,7,11]

        h1 : 0 6 7 11
        h2 : 0 3 7 11
        h3 : 0 0 7 11
        h4 : 0 0 4 11
        h5 : 0 0 1 11
        h6 : 0 0 0 11
        h7 : 0 0 0 8
        h8 : 0 0 0 5

        k => [1,11]

        k = mid
        ans <= h
        k + 1
        """

        l, r = 1, max(piles)
        res = float("inf")

        while l <= r:
            k = (l+r) // 2
            time = 0

            for p in piles:
                time += math.ceil(p/k)
                
            if time <= h:
                res = min(res, k)
                r = k-1
            else:
                l = k + 1
        
        return res
                
                
