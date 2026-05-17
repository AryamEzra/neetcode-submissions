class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = len(prices)
        buy = prices[0]
        max_profit = 0
        for i in range(p):
            if buy > prices[i]:
                buy = prices[i]
            
            sell = prices[i]
            max_profit = max(max_profit, sell - buy)
        return max_profit

        