class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        # nums.sort()
        for num in nums: 
            res += [ i + [num] for i in res]
        return res