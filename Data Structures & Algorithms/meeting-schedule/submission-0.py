class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        print(intervals)
        l = len(intervals)
        for i in range(1,l):
            if intervals[i-1].end > intervals[i].start:
                return False
        
        return True