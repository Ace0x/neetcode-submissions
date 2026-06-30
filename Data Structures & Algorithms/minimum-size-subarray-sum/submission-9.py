class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        n = len(nums)

        if n == 0:
            return 0
        
        l = 0
        r = 1
        
        s = nums[l]
        #print(l,r,s)
        ml = float('inf')

        while r < n and l < r:
            
            if s >= target:
                ml = min(r-l,ml)
            
            
            
            if s >= target:
                
                s -= nums[l]
                print(l,r,s)
                l += 1

            elif s < target:
                s += nums[r]
                print(l,r,s)
                r += 1
        
        while s >= target:
            ml = min(r-l,ml)
            s -= nums[l]
            l += 1
        print(s,ml)
        return ml if ml < float('inf') else 0