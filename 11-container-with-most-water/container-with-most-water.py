class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = 0

        while l < r:
            max_area = min(height[l], height[r]) * (r - l)
            res = max(max_area, res)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res