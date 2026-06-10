class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        memo = {}

        def dfs(i, holding):
            if i >= len(prices):
                return 0

            if (i, holding) in memo:
                return memo[(i, holding)]

            # do nothing today
            best = dfs(i + 1, holding)

            if holding:
                # sell today, then cooldown tomorrow, so jump to i + 2
                best = max(best, prices[i] + dfs(i + 2, False))
            else:
                # buy today
                best = max(best, -prices[i] + dfs(i + 1, True))

            memo[(i, holding)] = best
            return best

        return dfs(0, False)

            
