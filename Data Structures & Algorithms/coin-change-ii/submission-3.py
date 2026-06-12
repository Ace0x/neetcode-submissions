from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        memo = defaultdict(int)

        def dfs(i,c):
            if c == amount:
                return 1
            if i == len(coins):
                return 0
            if (i,c) in memo:
                return memo[(i,c)]
            
            if c > amount:
                return 0

            
            memo[(i,c)] += dfs(i,c+coins[i]) + dfs(i+1,c)

            return memo[(i,c)]
            
        return dfs(0,0)