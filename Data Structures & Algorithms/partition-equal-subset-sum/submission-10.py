class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        n = len(nums)
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if target == 0:
                return True
            if i >= n or target < 0:
                return False
            if memo[i][target] != -1:
                return memo[i][target]

            memo[i][target] = (dfs(i + 1, target) or
                               dfs(i + 1, target - nums[i]))
            return memo[i][target]

        return dfs(0, target)
        
        """if sum(nums) % 2:
            return False
        memo = {}
        
        def cp(i,s1,s2):
            if i >= len(nums):
                return s1 == s2
            if (i,s1) in memo:
                return memo[(i,s1)]
            

            if i == len(nums):
                return False

            skip = cp(i+1,s1,s2+nums[i])
            take = cp(i+1,s1+nums[i],s2)

            memo[(i,s1)] = skip or take

            return memo[(i,s1)]


        return cp(0,0,0)
"""