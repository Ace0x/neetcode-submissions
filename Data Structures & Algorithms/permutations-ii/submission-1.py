class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = []
        t = []
        used = [False] * n

        def dfs():
            if len(t) == n:
                res.append(t[:])   # copy current permutation
                return

            for i in range(n):
                if used[i]:
                    continue

                # skip duplicate branch
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue

                used[i] = True
                t.append(nums[i])

                dfs()

                t.pop()
                used[i] = False

        dfs()
        return res