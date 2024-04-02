class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        prefix = 1
        res = []
        for n in nums:
            res.append(prefix)
            prefix *= n

        postfix = 1
        for n in range(len(nums)-1, -1 ,-1):
            res[n] *= postfix
            postfix *= nums[n]
        return res