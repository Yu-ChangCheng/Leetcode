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
        # find the mid of the list using slow and fast pointer
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # mid of the list is the slow.next
        second = slow.next
        slow.next = None # disconnect the first list and second list

        prev = None # reverse the second list
        while second: 
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # combine two list
        first = head
        second = prev
        while second: # be careful since list2 is shorter than list 1 so the last node would be from list1
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2
        



