class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        memo = {}
        
        def cp(i,s1,s2):
            if i >= len(nums):
                return s1 == s2
            if (i,s1) in memo:
                return memo[(i,s1)]
            

            if i == len(nums):
                return False

            skip = cp(i+1,s1,s2+nums[i])
            take = cp(i+1,s1+nums[i],s2)

            memo[(i,s1)] = skip or take

            return memo[(i,s1)]


        return cp(0,0,0)
