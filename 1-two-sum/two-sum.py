class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i, a in enumerate(nums):
            complement = target - a
            if a in hashmap:
                return [i, hashmap[a]]
            else:
                hashmap[complement] = i
        