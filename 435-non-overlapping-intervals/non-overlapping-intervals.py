class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        res = 0
        intervals.sort()
        last_end = intervals[0][1]

        res = 0
        intervals.sort()
        last_end = intervals[0][1]
        for i in range(1,len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            if next_start < last_end:
                res += 1
                last_end = min(last_end, next_end)
            else:
                last_end = next_end
        return res
        
        for i in range(1, len(intervals)):
            next_start = intervals[i][0]
            next_end = intervals[i][1]
            if next_start < last_end:
                res += 1
                last_end = min(last_end, next_end)
            else:
                last_end = next_end
        return res