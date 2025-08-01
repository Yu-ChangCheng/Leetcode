# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0, head)
        prev = dummy

        while True:
            # 1) Check there are k nodes ahead
            tail = prev
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next

            # 2) Head-insertion: move each of the k–1 nodes
            #    after prev.next up to immediately after prev
            curr = prev.next
            for _ in range(k-1):
                nxt = curr.next
                curr.next      = nxt.next     # unlink nxt
                nxt.next       = prev.next    # splice nxt in front
                prev.next      = nxt

            # 3) Advance prev to the tail of this reversed block
            prev = curr
