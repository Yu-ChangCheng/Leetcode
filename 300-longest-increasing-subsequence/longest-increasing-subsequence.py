class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            for j in range(i, len(nums)):
                if nums[j] - nums[i] > 0:
                    LIS[i] = max(LIS[i], LIS[j] + 1)
        return max(LIS)