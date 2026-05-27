from collections import defaultdict
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        steps = float('inf')
        prev = 0
        memo = defaultdict(lambda: float('inf'))
        def jumper(i,prev,cnt):
            #print(i,prev,cnt)
            if i >= n - 1:
                #steps = min(steps,cnt)
                return cnt
            if i in memo:
                return memo[i]
            
            if i == prev:
                return float("inf")
            
            maxj = nums[i]
            #print(memo)
            for j in range(maxj,0,-1):
                
                memo[i] = min(memo[i],jumper(i+j,i,cnt+1))
            
            return memo[i]
        
        
        jumper(0,-1,0)
        #print(memo)
        return memo[0]