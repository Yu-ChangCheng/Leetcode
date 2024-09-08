class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []

        if not intervals:
            return [newInterval]

        for i in range(len(intervals)):
            # if new_intervel ends before the start just append it and the rest 
            if newInterval[1] <  intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if new_intervel start after the end just append the interval in to res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # we keep updating newIntervals until we finished the merge
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]

        res.append(newInterval)
        return res