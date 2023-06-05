# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False

        slow, fast = head, head.next

        while slow:
            if slow == fast:
                return True
            if not slow or not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return False