class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cur_sum = -float('inf')
        max_sum = -float('inf')

        for n in nums:
            if cur_sum < 0:
                cur_sum = 0
            cur_sum = cur_sum + n
            max_sum = max(cur_sum, max_sum)
        return max_sum