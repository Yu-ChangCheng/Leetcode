# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import heappush, heappop
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        min_heap = []
        for idx, node in enumerate(lists):
            if node:
                heappush(min_heap, (node.val, idx))
            
        head = ListNode()
        dummy = head

        while min_heap:
            val, idx = heappop(min_heap)
            head.next = lists[idx]
            head = head.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(min_heap, (lists[idx].val, idx))
        return dummy.next

