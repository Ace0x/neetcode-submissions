import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def eucl(x1,y1):
            x2 = 0
            y2 = 0
            return math.sqrt((0-x1)**2+(0-y1)**2)
        L = []
        heapq.heapify(L)
        for p in points:
            dist = eucl(p[0],p[1])
            heapq.heappush(L,(dist,p))
        
        res = []
        #print(L)
        for i in range(k):
            if len(L) <= 0:
                break
            res.append(heapq.heappop(L)[1])
        return res