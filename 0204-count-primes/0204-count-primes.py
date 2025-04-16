class Solution:
    def countPrimes(self, n: int) -> int:
        def sieve(x):
            if x < 2:
                return 0
            
            prime = [1 for _ in range(x+1)]
            prime[0] = 0
            prime[1] = 0

            p = 2

            while p * p <= x:
                if prime[p]:
                    for multiple in range(p * p, x+1, p):
                        prime[multiple] = 0
                p += 1
            
            return len([i for i,N in enumerate(prime) if N == 1 and i < x])
        
        return sieve(n)
