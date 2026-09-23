class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0, 1
        profit = 0
        low_price = 0
        while l<r and r < len(prices):
            if prices[r] > prices[l]:
                diff = prices[r] - prices[l]
                profit = max(profit, diff)
                print(profit)
            
            else:
                l = r
            r += 1
        return profit
            
            
            
            