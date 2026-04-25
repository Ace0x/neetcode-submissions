class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) -1

        while nums[l] > nums[r]:
            mid = l + (r - l) // 2
            print(l)
            print(r)
            print(mid)
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
            
