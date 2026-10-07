class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        prefix = 0
        seen = {0: 1}

        for num in nums:
            prefix += num

            result += seen.get(prefix - k, 0)

            seen[prefix] = seen.get(prefix, 0) + 1

        return result