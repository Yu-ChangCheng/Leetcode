class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l = 0 
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res