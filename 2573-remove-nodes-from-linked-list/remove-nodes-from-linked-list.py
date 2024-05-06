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
        stack = []

        curr = head

        while curr:
            while stack and stack[-1].val < curr.val:
                stack.pop()
            stack.append(curr)
            curr = curr.next
        # print(stack)
        
        head = ListNode()
        dummy = head
        for n in stack:
            head.next = n
            head = head.next
        # print(dummy)
        return dummy.next
        
        

