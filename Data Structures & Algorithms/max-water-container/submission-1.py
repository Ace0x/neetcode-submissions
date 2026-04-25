class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        i = 0
        j = len(heights) - 1
        while i < j:    
            h = min(heights[i],heights[j])
            b = j - i
            a = h * b
            if a > m:
                m = a
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return m
                 
                