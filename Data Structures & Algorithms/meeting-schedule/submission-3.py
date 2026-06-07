"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        intervals.sort(key = lambda x:x.start)
        if len(intervals) <= 1:
            return True

        l = intervals[0].start
        r = intervals[0].end
        #print(l,r)
        for i in intervals[1:]:
            #print(i.start,i.end)
            cl, cr = i.start, i.end
            if cl < r:
                return False
            i = cl
            r = cr
        


        return True