class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def r(i, s, f):
            if i <= -1:
                return s

            if (i, s, f) in memo:
                return memo[(i, s, f)]

            if i == len(nums) - 1:
                take = r(i - 2, s + nums[i], True)
            elif i == 0 and f:
                take = r(i - 2, s, f)
            else:
                take = r(i - 2, s + nums[i], f)

            skip = r(i - 1, s, f)

            memo[(i, s, f)] = max(skip, take)
            return memo[(i, s, f)]

        return r(len(nums) - 1, 0, False)


