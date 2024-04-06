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
            temp = curr.next #(2) (3)
            curr.next = prev #(->None) (->1)
            prev = curr #(None to 1) (2)
            curr = temp #(2) (3)
        return prev