class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                # Profitable? Check if it's the max, then look for a higher sell
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                # Price dropped? Found a new lowest valley.
                # "Jump" l to r. We found a better buy price.
                l = r
            
            # Always move r forward to check the next day
            r += 1
        return max_profit