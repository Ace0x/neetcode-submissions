class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        dic = dict()
        mult = 1
        res = [0] * len(nums)
        c = 0
        for i in nums:
            if i == 0:
                c += 1
            else:
                mult *= i
        if c >= 2:
            return res
        for i in range(len(nums)):
            if c > 0 and nums[i] != 0:
                res[i] = 0
            else:
                if nums[i] == 0:
                    res[i] = mult
                else:    
                    res[i] = mult // nums[i]
        return res
        