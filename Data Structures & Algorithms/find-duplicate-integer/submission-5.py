class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            # Use absolute value because we might have made this number negative earlier
            val = abs(nums[i])
            
            # If the number at this target index is ALREADY negative, 
            # we've been here before. We found the duplicate!
            if nums[val - 1] < 0:
                return val
            
            # Otherwise, mark the index as visited by flipping its sign to negative
            nums[val - 1] = -nums[val - 1]
            
        return -1