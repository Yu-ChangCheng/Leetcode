class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        stack = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)
        
        heights.pop()
        return max_area


        heights.append(0)  # Append a zero to ensure all elements are processed
        stack = [-1]  # Initialize stack with -1 as a dummy index
        max_area = 0  # This will store the maximum area

        for i in range(len(heights)):
            # While the current height is less than the height of the bar at the top of the stack
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Pop the stack and get the height
                w = i - stack[-1] - 1  # Calculate the width using the current index and top of the stack
                max_area = max(max_area, h * w)  # Update the maximum area
            stack.append(i)  # Push the current index onto the stack

        heights.pop()  # Remove the 0 that we added earlier
        return max_area  # Return the maximum area
