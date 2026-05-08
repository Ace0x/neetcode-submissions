class Solution:
    def rob(self, nums: List[int]) -> int:
        mula = 0
        bag = {}
        def rob(i):
            if i >= len(nums):
                return 0
            if bag.get(i):
                return bag[i]

            #print(mula,nums[i],i)
            mula_take = nums[i] + rob(i+2)
            
            mula_skip = rob(i+1) 
            
            bag[i] = max(mula_take,mula_skip)

            return bag[i]
        
        return rob(0)