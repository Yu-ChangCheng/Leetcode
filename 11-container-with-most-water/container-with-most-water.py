class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0 
        l, r = 0, len(height) - 1

        while l < r:
            width = r - l
            minheight = min(height[l], height[r])
            area = width * minheight
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return res