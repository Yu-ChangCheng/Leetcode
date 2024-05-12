class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water = 0
        leftMax = 0
        rightMax = 0
        # find the highest index in the middle
        highest_index = 0
        for i in range(len(height)):
            if height[i] > height[highest_index]:
                highest_index = i
        
        # count the water from left
        for i in range(highest_index):
            if height[i] > leftMax:
                leftMax = height[i]
            else:
                water += leftMax - height[i]

        # count the water from right
        for i in range(len(height)-1, highest_index, -1):
            if height[i] > rightMax:
                rightMax = height[i]
            else:
                water += rightMax - height[i]
        return water
            