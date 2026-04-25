class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def subset(ls,i):

            if i >= len(nums):
                res.append(ls.copy())
                return
            #print(ls, ' ', i)
            #append
            ls.append(nums[i])
            subset(ls,i+1)

            while i+1<len(nums) and nums[i] == nums[i+1]:
                i+=1
            #undo
            ls.pop()
            subset(ls,i+1)

        subset([],0)
        return res