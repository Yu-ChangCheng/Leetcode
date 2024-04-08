class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow, fast = 0, 0
        # find the slow pointer location
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # nums = [1,3,4,2,2]
        # 0->1->3->2->4->2->4->2->4
        # find the intersection due to the distance between the start point to the goal point would be the same as the slow point to the goal point
        begin = 0
        while True:
            begin = nums[begin]
            slow = nums[slow]
            if begin == slow:
                return slow