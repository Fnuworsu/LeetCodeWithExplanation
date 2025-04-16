class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
            
        def prime_factors(n):
            factors = []

            # Step 1: Factor out 2s
            while n % 2 == 0:
                factors.append(2)
                n //= 2

            # Step 2: Factor odd numbers from 3 to sqrt(n)
            p = 3
            while p * p <= n:
                while n % p == 0:
                    factors.append(p)
                    n //= p
                p += 2

            # Step 3: If n is still greater than 1, it's prime
            if n > 1:
                factors.append(n)

            return set(factors)
        
        cache = {2,3,5}
        prime = prime_factors(n)
        print(prime)

        for x in prime:
            if x not in cache:
                return False
        
        return True

        

                