class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = len(prices)
        max_profit = 0
        for i in range(p-1):
            buy = prices[i]
            check = prices[i+1:]
            # print(check)
            sell = max(check)
            max_profit = max(max_profit, sell - buy)
        return max_profit

        