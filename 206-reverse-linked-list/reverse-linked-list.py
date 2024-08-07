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
        # 1 -> 2 -> 3 -> None
        if not head or not head.next:
            return head

        # return the reverse_head
        reverse_head = self.reverseList(head.next) # head = 2, reverse_head = 3

        # recursion start to reverse
        head.next.next = head # 2.next.next = 2 
        # 1 -> 2 <-> 3
        head.next = None # 2 -> None
        # 1 -> 2 <- 3

        return reverse_head # return 3


        


        # prev = None #(None)
        # curr = head #(1)

        # while curr:
        #     next_node = curr.next #(2) / (3)
        #     curr.next = prev #(->None) / (->1)
        #     prev = curr #(None to 1) / (2)
        #     curr = next_node #(2) / (3)
        # return prev