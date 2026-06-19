class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for i in nums:
            count[i] += 1
        
        j = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[j] = i
                j += 1