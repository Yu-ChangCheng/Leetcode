class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 2:
            return max(nums)
        
        if nums[0]>nums[1]:
            nums[1] = nums[0]

        for i in range(2,n):
            nums[i] = max(nums[i-2]+nums[i], nums[i-1])
        
        return nums[-1]