class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if sum(nums) % 2 != 0:
            return False
        
        dp = set()
        target = sum(nums) // 2
        dp.add(0)

        for i in range(len(nums)):
            for t in dp.copy():
                dp.add(t)
                dp.add(nums[i]+t)
        return True if target in dp else False
