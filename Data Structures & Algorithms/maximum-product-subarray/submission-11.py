class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        res = max(nums)
        cmax, cmin = 1,1
        for n in nums:
            if n == 0:
                cmax,cmin =  1,1
            else:
                tmp = cmax
                
                cmax = max(cmax*n,cmin*n,n)
                cmin = min(tmp*n,cmin*n,n)
                #print(cmax,cmin)
                res = max(res,cmax,cmin)
        return res

