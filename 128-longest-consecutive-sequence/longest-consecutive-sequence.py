class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        numSet = set(nums)
        maxlength = 0

        for i in nums:
             if (i - 1) not in numSet:
                length = 0
                while i + length in numSet:
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength