import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        best = r
        while l <= r:

            mid = (l + r) // 2
            accum = 0
            for i in piles:
                accum += math.ceil(i/mid)
            if accum > h:
                l = mid + 1
            else:
                best = mid
                r = mid - 1
        return best

