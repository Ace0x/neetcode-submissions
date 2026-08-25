class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        n = len(nums)
        memo = {}

        def dfs(mask, current_sum):
            # Everyone has been used
            if mask == (1 << n) - 1:
                return True

            # Important:
            # current_sum is always the sum of the current bucket,
            # modulo target.
            key = (mask, current_sum)

            if key in memo:
                return memo[key]

            for i in range(n):
                # already used
                if mask & (1 << i):
                    continue

                new_sum = current_sum + nums[i]

                if new_sum > target:
                    continue

                new_mask = mask | (1 << i)

                # If bucket reaches target, begin a new bucket
                next_sum = 0 if new_sum == target else new_sum

                if dfs(new_mask, next_sum):
                    memo[key] = True
                    return True

            memo[key] = False
            return False

        return dfs(0, 0)