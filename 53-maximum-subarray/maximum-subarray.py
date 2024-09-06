class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum = -float('inf')
        max_sum = -float('inf')

        for n in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum = curr_sum + n
            max_sum = max(curr_sum, max_sum)
        return max_sum
