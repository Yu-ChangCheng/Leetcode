class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        total = (n*(n+1))//2
        nums_total =sum(nums)
        return total-nums_total