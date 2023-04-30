class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda i: i[0])
        output = [intervals[0]]
 
        for start, end in intervals:
            lastEnd = output[-1][1]

            if lastEnd >= start:
                output[-1][1] = max(end, output[-1][1])
            else:
                output.append([start,end])
        return output

        