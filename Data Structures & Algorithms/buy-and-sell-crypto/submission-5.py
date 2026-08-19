class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = len(prices)
        ans = 0
        for i in range(p-1):
            buy = prices[i]
            arr = prices[i+1:]
            sell = max(arr)
            ans = max(ans, sell - buy)
            
            
        return ans


        