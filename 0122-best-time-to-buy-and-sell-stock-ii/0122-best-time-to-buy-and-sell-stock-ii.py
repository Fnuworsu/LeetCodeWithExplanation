class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0

        for i in range(1, len(prices)):
            buy = prices[i-1]
            nxt = prices[i]
            p = 0

            if nxt < buy:
                buy = nxt
            else:
                p = max(p, nxt-buy)
                maxP += p

        return maxP            
        