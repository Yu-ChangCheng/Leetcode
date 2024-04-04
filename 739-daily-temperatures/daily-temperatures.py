class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = [] #[index, value]
        res = [0] * len(temperatures)
        
        for i, val in enumerate(temperatures):
            while stack and stack[-1][1] < val:
                stack_ind, stack_value = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append([i,val])
        return res

                