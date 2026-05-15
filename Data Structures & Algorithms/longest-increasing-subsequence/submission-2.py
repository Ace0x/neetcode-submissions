class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        """mx = float('-inf')

        cache = {}


        def lol(i, cnt, curr):
            if i == len(nums):
                return cnt

            if (i, cnt, curr) in cache:
                return cache[(i, cnt, curr)]

            # skip nums[i]
            b2 = lol(i + 1, cnt, curr)

            # take nums[i], if valid
            b1 = 0
            if curr < nums[i]:
                b1 = lol(i + 1, cnt + 1, nums[i])

            cache[(i, cnt, curr)] = max(b1, b2)
            return cache[(i, cnt, curr)]

        return lol(0,0,mx)"""