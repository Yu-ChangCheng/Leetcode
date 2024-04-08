class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        begin = 0
        while True:
            begin = nums[begin]
            slow = nums[slow]
            if slow == begin:
                return slow