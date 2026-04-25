import math
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        s = set(nums)
        best = 0
        chain = 1
        for i in s:
            if i - 1 not in s:
                curr = i
                #print("curr: ",curr)
                chain = 1
                while True:
                    if curr + 1 in s:
                        chain += 1
                        curr += 1
                        #print("itr:" ,curr, "chain: ",chain)
                    else:
                        if chain > best:
                            best = chain 
                        break
            
        return best
        """
        for i in range(len(arr)):
            #print("arr: ",arr[i])
            #print("prev: ",prev)
            if arr[i] - prev == 1:
                chain += 1
            else:
                if chain > best:
                    best = chain
                chain = 0
            prev = arr[i]
        if chain > best:
            best = chain
        
        """
        return best + 1