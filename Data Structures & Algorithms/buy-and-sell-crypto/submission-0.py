class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        profit = 0
        curr = 0

        for r in range(1, len(prices)):

            while prices[r] < prices[l] and l != r:
                l = l + 1

            curr = prices[r] - prices[l]
            profit = max(profit, curr)
        
        return profit


        
        