import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.l = nums
        heapq.heapify(nums)
        self.maxh = nums
    def add(self, val: int) -> int:
        print(self.maxh)
        heapq.heappush(self.maxh, val)
        while len(self.maxh) > self.k:
            heapq.heappop(self.maxh)
        return min(self.maxh)

    #is this even good? idk? like it works but not efficient noooooo

        
