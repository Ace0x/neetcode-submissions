class Solution:
    def rob(self, nums: List[int]) -> int:
        mula = 0
        bag = {}
        def rob(i,mula):
            if i >= len(nums):
                return 0
            if bag.get(i):
                return bag[i]

            #print(mula,nums[i],i)
            mula_take = nums[i] + rob(i+2,mula)
            
            mula_skip = rob(i+1,mula) 
            
            bag[i] = max(mula_take,mula_skip)
            
            return bag[i]
        
        return rob(0,0)