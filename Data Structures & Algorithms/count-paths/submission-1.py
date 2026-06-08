from collections import defaultdict
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m == 1 and n == 1:
            return 1
        memo = defaultdict(int)
        
        def dfs(i,j):
            if not (i < m and i >= 0 and j < n and j >= 0):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if i == m - 1 and j == n - 1:
                return 1
            
            
            memo[(i,j)] += dfs(i+1,j)

            memo[(i,j)] += dfs(i,j+1)


            return memo[(i,j)]
        dfs(0,0)
        return memo[(0,0)]