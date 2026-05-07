class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """def dfs(tc, i):
            if i >= len(cost):
                return tc
            
            curr = tc
            if i >= 0:
                curr += cost[i]

            return min(
                dfs(curr, i + 1),
                dfs(curr, i + 2)
            )

        return dfs(0, -1)"""
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(dfs(i + 1),dfs(i + 2))

            return memo[i]

        
        return min(dfs(0),dfs(1))