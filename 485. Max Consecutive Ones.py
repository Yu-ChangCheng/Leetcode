class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        Max_count = 0
        if len(nums) == 0:
            return 0
        for i in nums:
            if i == 1:
                count += 1
            else:
                if count >= Max_count:
                    Max_count = count
                count = 0
        return max(Max_count,count)
