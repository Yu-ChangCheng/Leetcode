# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        # slow and fast to find the midpoint to break into two list
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reset second to the first.next so it is the start of the second list
        second = slow.next
        # remove the link from first to the second list
        prev = slow.next = None

        # reverse the second list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # merge two list
        second = prev
        first = head

        # firstlist = [1,2,3]
        # secondlist = [9,8,7]
        # first = 1
        # second = 9

        while second:
            temp1 = first.next # 2
            temp2 = second.next # 8
            first.next = second # 1->9
            second.next = temp1 # 1->9->2->8
            first = temp1 # (first 2)
            second = temp2 # (seecond 8)

