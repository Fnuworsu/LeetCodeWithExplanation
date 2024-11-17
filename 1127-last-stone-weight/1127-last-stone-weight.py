class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        [8,7,4,2,1,1]
         0 1 2 3 4 5
         1 0 2 0 0  0   
        """
        #Brute Force Solution
        if len(stones) == 1: return stones[0]

        stones.sort(reverse = True)

        for i in range(len(stones)):
            
            x, y = stones[1], stones[0]
            if x == y:
                stones[1], stones[0] = 0, 0
                stones.sort(reverse = True)
            else:
                stones[1], stones[0] = 0, y-x    
                stones.sort(reverse = True)

        return sum(stones)            
        