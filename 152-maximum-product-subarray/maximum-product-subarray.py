class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max = nums[0]
        curr_min = nums[0]
        res = nums[0]

        for n in nums[1:]:
            next_max = n * curr_max
            next_min = n * curr_min

            curr_max = max(n, next_max, next_min)
            curr_min = min(n, next_max, next_min)
            res = max(res, curr_max)
        return res
        
