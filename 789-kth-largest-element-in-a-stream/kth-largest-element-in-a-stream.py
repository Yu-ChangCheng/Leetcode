class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minheap = nums
        heapq.heapify(self.minheap)
        while len(self.minheap) > k:
            heapq.heappop(self.minheap)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minheap) == self.k:
            heapq.heappushpop(self.minheap, val)
        else:
            heapq.heappush(self.minheap, val)
        return self.minheap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)