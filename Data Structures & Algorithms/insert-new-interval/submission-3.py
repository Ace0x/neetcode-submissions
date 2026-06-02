class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        res = []
        f = 0
        l,r = newInterval[0],newInterval[1]

        for i in intervals:
            a = i[0]
            b = i[1]
            #print(a,b,l,r)
            if f:
                res.append([a,b])
                continue
            if l >= a and l<=b:
                l = a
                r = max(r,b)
                continue
            if r <=b and r >= a:
                r = b
                l = min(l,a)
                continue
            if r >= b and l <=a:
                continue
            if a > r:
                res.append([l,r])
                res.append([a,b])
                f = 1
                continue
            res.append([a,b])
        
        if not f:
            res.append([l,r])
        return res