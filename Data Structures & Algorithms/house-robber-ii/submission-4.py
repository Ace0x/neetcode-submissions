class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        
        def r(i, took_last):
            if i < 0:
                return 0

            if (i, took_last) in memo:
                return memo[(i, took_last)]

            # If we took the last house, we cannot take house 0
            if i == 0 and took_last:
                take = 0
            else:
                take = nums[i] + r(i - 2, took_last)

            skip = r(i - 1, took_last)

            memo[(i, took_last)] = max(take, skip)
            return memo[(i, took_last)]

        if len(nums) == 1:
            return nums[0]

        # Case 1: force possibility of taking last house
        take_last = nums[-1] + r(len(nums) - 3, True)

        # Case 2: skip last house
        skip_last = r(len(nums) - 2, False)

        return max(take_last, skip_last)

