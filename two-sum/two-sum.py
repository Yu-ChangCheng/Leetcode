class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for index, value in enumerate(nums):
            key = target - value
            if key in seen:
                return [seen[key], index]
            else:
                seen[value] = index