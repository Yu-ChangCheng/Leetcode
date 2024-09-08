class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        curr_interval = intervals[0]
        res = []
        for i in range(1,len(intervals)):
            if curr_interval[1] < intervals[i][0]:
                res.append(curr_interval)
                curr_interval = intervals[i]
            else:
                curr_interval = (min(intervals[i][0], curr_interval[0]), max(intervals[i][1], curr_interval[1]))
        res.append(curr_interval)
        return res