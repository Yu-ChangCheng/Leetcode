class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True
        return False