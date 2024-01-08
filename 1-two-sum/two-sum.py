class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = defaultdict(int)

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement not in hashmap:
                hashmap[nums[i]] = i
            else:
                return [i, hashmap[complement]]
