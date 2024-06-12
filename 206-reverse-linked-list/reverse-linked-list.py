# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

        prev = None
        curr = head

        while curr:
            next_node = curr.next #(2) (3)
            curr.next = prev #(->None) (->1)
            prev = curr #(None to 1) (2)
            curr = next_node #(2) (3)
        return prev