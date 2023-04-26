class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        current_Subarray_Sum = 0
        max_Sum = -99999999

        for i in range(len(nums)):
            current_Subarray_Sum = max(nums[i],current_Subarray_Sum+nums[i])
            max_Sum = max(max_Sum,current_Subarray_Sum)
        return(max_Sum)
            
