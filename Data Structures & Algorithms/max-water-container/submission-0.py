class Solution:
    def maxArea(self, heights: List[int]) -> int:
        m = 0
        for i in range(len(heights)):
            
            for j in range(len(heights)-1,i,-1):
            
                h = min(heights[i],heights[j])
                b = j - i
                a = h * b
                if a > m:
                    m = a
        return m
                 
                