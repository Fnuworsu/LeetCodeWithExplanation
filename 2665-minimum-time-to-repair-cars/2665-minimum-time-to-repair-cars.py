class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        """
        x = r * n**2
        n = (x/r) ** 0.5

        max rank = 10**2
        max cars = 10**6

        max time = max rank x max cars

        """
        def sufficient(time):
            cars_done = 0

            for r in ranks:
                n = (time // r) ** (0.5)
                cars_done += int(n)
            
            return cars_done >= cars

        l, r = 1, 10**14
        res = float("inf")

        while l <= r:
            mid = (l + r) // 2

            if sufficient(mid):
                res = min(res,mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
        