class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                return True
        return False
