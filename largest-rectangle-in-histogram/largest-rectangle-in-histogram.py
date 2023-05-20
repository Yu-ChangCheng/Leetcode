class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = [] # [(index, height)]
        maxArea = 0

        for curr_index, curr_height in enumerate(heights):
            start = curr_index
            while stack and curr_height < stack[-1][1]:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (curr_index - index))
                start = index
            stack.append((start, curr_height))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
            
        return maxArea