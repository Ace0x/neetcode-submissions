class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(i, s):
            if s == amount:
                return 0

            if s > amount:
                return float('inf')

            if i >= len(coins):
                return float('inf')

            if (i, s) in memo:
                return memo[(i, s)]

            skip = dfs(i + 1, s)
            take_once_then_move = 1 + dfs(i + 1, s + coins[i])
            take_and_stay = 1 + dfs(i, s + coins[i])

            memo[(i, s)] = min(skip, take_once_then_move, take_and_stay)
            return memo[(i, s)]

        res = dfs(0, 0)
        return res if res != float('inf') else -1