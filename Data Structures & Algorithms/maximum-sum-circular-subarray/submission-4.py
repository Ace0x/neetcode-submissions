class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        this should technically work due to recursion limit tho.
        n = len(nums)
        memo = {}

        def dfs(i, s, skipped):
            # Not started, and we have skipped every possible start.
            # Empty subarray is invalid.
            if s == float('inf') and skipped == n:
                return float('-inf')

            # Already started, and we wrapped back to the start.
            # Stop before reusing the same index.
            if s != float('inf') and i == s:
                return 0

            if (i, s, skipped) in memo:
                return memo[(i, s, skipped)]

            if s == float('inf'):
                # Option 1: start subarray at i
                start = nums[i] + dfs((i + 1) % n, i, 0)

                # Option 2: skip i and keep looking for a start
                skip = dfs((i + 1) % n, float('inf'), skipped + 1)

                memo[(i, s, skipped)] = max(start, skip)

            else:
                # Option 1: continue the current subarray
                take = nums[i] + dfs((i + 1) % n, s, 0)

                # Option 2: stop the subarray here
                stop = 0

                memo[(i, s, skipped)] = max(take, stop)

            return memo[(i, s, skipped)]

        return dfs(0, float('inf'), 0)
        """
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        suffix_sum = nums[-1]

        for i in range(n - 2, -1, -1):
            suffix_sum += nums[i]
            right_max[i] = max(right_max[i + 1], suffix_sum)

        max_sum = nums[0]
        cur_max = 0
        prefix_sum = 0

        for i in range(n):
            cur_max = max(cur_max, 0) + nums[i]
            max_sum = max(max_sum, cur_max)
            prefix_sum += nums[i]
            if i + 1 < n:
                max_sum = max(max_sum, prefix_sum + right_max[i + 1])

        return max_sum
