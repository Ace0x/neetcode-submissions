class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) -1

        while nums[l] > nums[r]:
            mid = (r - l) // 2
            if nums[mid] > nums[r]:
                l = l + 1
            else:
                r = r - 1
        return nums[l]
            
