class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        1.Greedily buy the stock with the lowest cost
        2.If we are already at the lowest stock we can buy, we calculate and update our maxProfit
        """
        buy = prices[0]
        maxProfit = 0

        for price in prices[1:]:
            if buy > price:
                buy = price
            else:
                profit = price - buy
                maxProfit = max(maxProfit, profit)

        return maxProfit            

        