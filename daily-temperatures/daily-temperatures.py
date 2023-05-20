class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [0] * len(temperatures)
        for i, curr in enumerate(temperatures):
            if not stack:
                stack.append((i,curr))
            else:
                while stack and curr > stack[-1][1]:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()
                stack.append((i,curr))
        return res


                