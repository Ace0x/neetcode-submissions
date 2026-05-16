class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        memo = {}
        
        def cp(i,s1,s2):
            if (i,s1,s2) in memo:
                return memo[(i,s1,s2)]
            if s1 == s2 and i >= len(nums):
                return True

            if i == len(nums):
                return False

            skip = cp(i+1,s1,s2+nums[i])
            take = cp(i+1,s1+nums[i],s2)

            memo[(i,s1,s2)] = skip or take

            return memo[(i,s1,s2)]


        return cp(0,0,0)
