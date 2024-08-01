# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
            head.next =lists[idx]
            head = head.next
            lists[idx] = lists[idx].next
            if lists[idx]:
                heappush(min_heap,(lists[idx].val, idx))
        return dummy.next

        if not lists or len(lists) == 0:
            return None
        

        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]

    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next= l2
                l2 = l2.next
            tail = tail.next
        if l2:
            tail.next = l2
        if l1:
            tail.next = l1
        return dummy.next

                