class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if it is odd then return false
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()
        target = sum(nums) // 2
        dp.add(0) # have 0 as intial value

        for i in range(len(nums)):
            for t in dp.copy():
                dp.add(nums[i]+t)
        return True if target in dp else False
