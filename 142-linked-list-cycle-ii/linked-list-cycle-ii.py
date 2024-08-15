# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        
        # find the cycle and the point where slow meets fast
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        
        if not fast or not fast.next:
            return None

        # start from begining 
        slow = head
        while fast:          # while slow!= fast:
            if slow == fast:
                return slow
            slow = slow.next
            fast = fast.next

        