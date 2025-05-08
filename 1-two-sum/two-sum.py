class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i, val in enumerate(nums):
            remainder = target - val
            if remainder not in hashmap:
                hashmap[val] = i
            else:
                return [hashmap[remainder], i]