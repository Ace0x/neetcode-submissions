class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []
        def dfs(i,s):
            if s > target or i >= len(nums):
                return
            if s == target:
                res.append(cur.copy())
                return
            cur.append(nums[i])
            dfs(i,s+nums[i])

            x = cur.pop()
            dfs(i+1,s-x+nums[i])
        dfs(0,0)
        return res