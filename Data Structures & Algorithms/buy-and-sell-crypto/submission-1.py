class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p = len(prices)
        max_ans = 0
        cur_min = float('inf')

        for r in range(p): 
            if cur_min > prices[r]:
                cur_min = min(prices[r], cur_min)
            max_ans = max(max_ans, prices[r] - cur_min)
        return max_ans