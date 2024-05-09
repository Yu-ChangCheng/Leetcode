class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return max(nums)
        
        nums[1] = max(nums[0], nums[1])
        for i in range(2,len(nums)):
            nums[i] = max((nums[i] + nums[i-2]), nums[i-1])
        print(nums)
        return nums[-1]
