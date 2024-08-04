class Solution:
    def maximumMeetings(self, n, start, end):
        meetings = [(start[i], end[i]) for i in range(n)]
        meetings.sort(key=lambda x: (x[1], x[0]))
        max_meetings = 0
        last_end_time = -1
        for meeting in meetings:
            if meeting[0] > last_end_time:
                max_meetings += 1
                last_end_time = meeting[1]
        
        return max_meetings
