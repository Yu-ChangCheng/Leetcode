class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height: return 0

        l = 0
        r = len(height) -1 
        res = 0
        leftMax = height[l]
        rightMax = height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                res += max(leftMax - height[l], 0)
                leftMax = max(leftMax, height[l])
            else:
                r -= 1
                res += max(rightMax - height[r], 0)
                rightMax = max(rightMax, height[r])
                
        return res