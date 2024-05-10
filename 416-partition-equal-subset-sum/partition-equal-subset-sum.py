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
            next_dp = set()
            for t in dp:
                next_dp.add(t)
                next_dp.add(t+nums[i])
            dp = next_dp
        return True if target in dp else False