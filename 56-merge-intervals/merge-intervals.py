class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        new_interval = intervals[0]
        res = []
        for i in range(1,len(intervals)):
            if new_interval[1] < intervals[i][0]:
                res.append(new_interval)
                new_interval = intervals[i]
            else:
                new_interval = (min(intervals[i][0], new_interval[0]), max(intervals[i][1], new_interval[1]))
        res.append(new_interval)
        return res