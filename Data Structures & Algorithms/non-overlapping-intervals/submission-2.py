class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals.sort(key = lambda x:x[1])
        #print(intervals)
        l = intervals[0][0]
        r = intervals[0][1]
        remove = 0

        for i in intervals[1:]:
            cl = i[0]
            cr = i[1]
            #print([l,r],[cl,cr],remove)
            if cl >= r:
                l = cl
                r = cr
            else:
                remove += 1
                

        return remove