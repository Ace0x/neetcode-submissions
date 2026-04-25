import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        L = []
        heapq.heapify_max(L)
        for i in nums:
            heapq.heappush_max(L,i)
        
        for i in range(k-1):
            heapq.heappop_max(L)
        
        return heapq.heappop_max(L)