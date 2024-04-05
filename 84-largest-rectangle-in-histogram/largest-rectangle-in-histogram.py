class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] #[index, value]
        maxArea = 0

        for curr_index, curr_val in enumerate(heights):
            start = curr_index
            while stack and curr_val < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (curr_index- index))
                start = index
            stack.append([start, curr_val])
        
        for i in range(len(stack)):
            index, h = stack.pop()
            maxArea = max(maxArea,(len(heights) - index) * h)
        return maxArea
