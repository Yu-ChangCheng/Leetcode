class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = defaultdict(int)
        for i, n in enumerate(nums):
            complement = target - n
            if complement not in hashmap:
                hashmap[n] = i
            else:
                return [hashmap[complement], i]