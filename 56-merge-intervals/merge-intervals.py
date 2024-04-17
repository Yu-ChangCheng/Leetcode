class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals, key = lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            if start <= output[-1][1]:
                output[-1][1] = max(output[-1][1], end) # remember to use max
            else:
                output.append([start, end])
        return output

        
            
