# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        stack = []

        while head:
            while stack and head.val > stack[-1].val:
                stack.pop()
            stack.append(head)
            head = head.next
            
        dummy = ListNode()
        head = dummy
        for node in stack:
            head.next = node
            head = head.next
        return dummy.next

            
