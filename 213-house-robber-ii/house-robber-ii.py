class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self,nums):
        rob1 = 0
        rob2 = 0
        for i in range(len(nums)):
            temp = rob2
            rob2 = max(rob1+nums[i], rob2)
            rob1 = temp
        return rob2