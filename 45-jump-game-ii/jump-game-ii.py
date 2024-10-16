class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, 0
        res = 0
        farest = 0

        while r < len(nums) - 1:
            for i in range(l, r + 1):
                farest = max(farest, i + nums[i])
            l = r + 1
            r = farest
            res += 1
        return res
        