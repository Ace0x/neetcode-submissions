class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = 1
        res = [1] * len(nums)
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]
        pos = 1
        for j in range(len(nums) - 1,-1,-1):
            res[j] *= pos
            pos *= nums[j]
        return res