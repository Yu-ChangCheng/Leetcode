class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        res = []
        new_start, new_end = newInterval
        merged = False
        #
        for i, (start, end) in enumerate(intervals):
        # [1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
            if end < new_start: # the current interval is before the newInterval
                res.append([start, end]) # append([1,2])
            elif start > new_end: # the current interval is after the newInterval
                res.append([new_start, new_end])
                merged = True
                return res+intervals[i:]
            else:
                new_start, new_end = min(start, new_start), max(end, new_end)
        
        if not merged:
            res.append([new_start, new_end])
        return res























        res = []

        for i in range(len(intervals)):
            # if new_intervel ends before the start just append it and the rest 
            if newInterval[1] <  intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # if new_intervel start after the end just append the interval in to res
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0],intervals[i][0]), max(newInterval[1],intervals[i][1])]
        res.append(newInterval)
        return res