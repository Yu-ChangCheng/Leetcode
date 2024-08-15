# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # node number is even
        # convert the list 1 -> 2 -> 2 -> 1 into using slow fast pointer, s at index 1, f at index 3
        # list 1, 1 -> 2 
        # list 2, 2 -> 1

        # reverse the list 2
        # list 1, 1 -> 2 
        # list 2, 1 -> 2
        # compare two list2

         # node number is odd
        # convert the list 1 -> 2 -> 3 -> 2 -> 1 into using slow fast pointer  s at index 2, f at index 5(none)
        # list 1, 1 -> 2 -> 3
        # list 2, 2 -> 1

        # reverse the list 2
        # list 1, 1 -> 2 -> 3
        # list 2, 1 -> 2
        # compare two list2 if any remaining list is empty after traversing meaning we have odd numbers we return True

        slow, fast = head, head.next

        # find mid point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # separate two lists and find the head of second list
        list2_head = slow.next
        slow.next = None

        # reverse the second list
        prev = None
        curr = list2_head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # two lists
        list1 = head
        list2 = prev

        # compare two list
        while list1 and list2:
            if list1.val != list2.val:
                return False
            else:
                list1 = list1.next
                list2 = list2.next
        
        return True




