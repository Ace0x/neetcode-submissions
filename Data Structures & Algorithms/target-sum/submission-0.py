from collections import defaultdict
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        memo = defaultdict(int)
        
        def dfs(i,c):
            if i == len(nums):
                if c == target:
                    return 1
                return 0
            if (i,c) in memo:
                return memo[(i,c)]

            minus = dfs(i+1,c-nums[i])
            plus = dfs(i+1,c+nums[i])

            memo[(i,c)] += minus + plus
            
            return memo[(i,c)]
        return dfs(0,0)