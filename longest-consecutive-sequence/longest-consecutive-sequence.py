class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numSet = set(nums)
        longest = 0
        
        for i in nums:
            length = 1
            if i-1 not in numSet:
                while i+1 in numSet:
                    length += 1
                    i += 1
                longest = max(length, longest)
        return longest