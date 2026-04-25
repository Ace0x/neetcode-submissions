class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        test = set()
        nums = sorted(nums)
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while r > l:
                a = nums[i]
                b = nums[l]
                c = nums[r]
                x = a + b + c
                if x == 0:
                    r -= 1
                    l += 1
                    if (a,b,c) in test:
                        continue
                    res.append([a,b,c])
                    test.add((a,b,c))
                if x > 0:
                    r -= 1
                if x < 0:
                    l += 1        
        return res
        