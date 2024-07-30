# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        #    [1,2,3,4,5]
        #.   l . r           n = 2

        Dummy = ListNode()
        Dummy.next = head

        # First to have two pointers with interval n
        slow = Dummy
        fast = head

        while n > 0 and fast:
            fast = fast.next
            n -= 1
        
        # Remember to move the fast pointer just by one in here as we want to keep distance n
        while fast:
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return Dummy.next


