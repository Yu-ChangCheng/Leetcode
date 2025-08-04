class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.minHeap = nums
        heapq.heapify(self.minHeap) # this replace in-place and won't return val so don't write self.minHeap = heapq.heapify(nums) 
                                    # will get only None type
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)



    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)