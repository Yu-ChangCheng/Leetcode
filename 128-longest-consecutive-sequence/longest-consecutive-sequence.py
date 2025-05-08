class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 1:
            return 0

        seen = set(nums)
        result = 1

        for n in seen:
            if n - 1 not in seen:
                count = 1
                while n + 1 in seen:
                    count += 1
                    n += 1
                result = max(result, count)
        return result
