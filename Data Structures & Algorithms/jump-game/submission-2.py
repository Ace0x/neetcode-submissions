class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        prev = 0
        i = 0
        memo = {}
        def canj(i):
            if i >= n - 1:
                return True

            if i in memo:
                return memo[i]

            max_jump = nums[i]

            for step in range(max_jump, 0, -1):
                if canj(i + step):
                    memo[i] = True
                    return True

            memo[i] = False
            return False
            
        return canj(0)