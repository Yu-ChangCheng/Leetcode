# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val > list2.val:
                tail.next = list2
                tail=tail.next
                list2 = list2.next
            else:
                tail.next = list1
                tail = tail.next
                list1 = list1.next
        if list2==None and list1 !=None:
            tail.next = list1
        elif list1==None and list2 !=None:
            tail.next = list2
        return dummy.next 