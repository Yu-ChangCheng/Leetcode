class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(range(len(nums)+1))
        nums_total =sum(nums)
        return total-nums_total