import heapq as h

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h.heapify_max(stones)
        while len(stones) > 1:
            a = h.heappop_max(stones)
            b = h.heappop_max(stones)
            if b < a:
                h.heappush_max(stones, a-b)
        if len(stones) != 0:
            return h.heappop_max(stones)
        else:
            return 0
            