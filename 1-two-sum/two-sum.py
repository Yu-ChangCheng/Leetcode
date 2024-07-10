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
        
        # Time: O(n) since it is a linear scan for the entire array
        # Space: O(n) since we have a hashmap to store the index

        