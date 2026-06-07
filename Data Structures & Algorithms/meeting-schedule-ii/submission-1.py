import heapq
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)

        rooms = []  # min-heap of meeting end times

        for meeting in intervals:
            # If the earliest room is free, reuse it
            if rooms and rooms[0] <= meeting.start:
                heapq.heappop(rooms)

            # Put current meeting into a room
            heapq.heappush(rooms, meeting.end)

        return len(rooms)