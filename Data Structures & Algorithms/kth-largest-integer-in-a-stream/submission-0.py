import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        heapq.heapify_max(nums)
        self.maxh = nums
    def add(self, val: int) -> int:
        print(self.maxh)
        heapq.heappush_max(self.maxh, val)
        uwu = []
        for i in range(self.k - 1):
            uwu.append(heapq.heappop_max(self.maxh))
        x = self.maxh[0]
        for i in range(self.k - 1):
            heapq.heappush_max(self.maxh, uwu[i])
        return x

        
