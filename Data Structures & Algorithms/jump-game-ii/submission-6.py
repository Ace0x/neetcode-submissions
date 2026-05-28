from collections import defaultdict
class Solution:
    def jump(self, nums: List[int]) -> int:
        """n = len(nums)
        memo = {}

        def jumper(i):
            if i >= n - 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            if nums[i] == 0:
                memo[i] = float("inf")
                return memo[i]
            
            best = float("inf")

            for j in range(1, nums[i] + 1):
                best = min(best, 1 + jumper(i + j))
            
            memo[i] = best
            return memo[i]
        
        return jumper(0)"""
        res = 0
        l = r = 0

        while r < len(nums) - 1:
            print(l,r)
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
                print(farthest)
            l = r + 1
            r = farthest
            res += 1
        return res