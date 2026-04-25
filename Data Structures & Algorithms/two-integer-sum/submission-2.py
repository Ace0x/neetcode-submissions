class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check = dict()
        for i in range(len(nums)):
            check[nums[i]] = i
        for i in range(len(nums)):
            x = target - nums[i]
            y = check.get(x,None)
            if y and i != y:
                return [i,y]
        return [0]