class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        """
        15/5 = 3
        12/5 = 3
        8/5 = 2

        1 to max

        15

        day1: 1 2 3 4 5
        day2: 

        for w in weigths:
            add += w
            if w > cap:
                count += 1
                count = 0
        """
        def ship(cap):
            count = 1
            items = 0

            for w in weights:
                if items + w > cap:
                    count += 1
                    items = 0
                
                items += w
            # print(count)
            return count <= days
        l,h = max(weights), sum(weights)
        res = float("inf")

        while l <= h:
            k = (l+h) // 2
            if ship(k):
                res = min(res, k)
                h = k-1
            else:
                l = k+1
        
        return res