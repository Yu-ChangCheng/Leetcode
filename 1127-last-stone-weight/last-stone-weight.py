class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        heap = []
        for i in stones:
            heapq.heappush(heap,-i)
        
        while len(heap) > 1:
            num_1 = heapq.heappop(heap)
            num_2 = heapq.heappop(heap)
            if num_1 == num_2:
                pass
            else:
                heapq.heappush(heap, num_1 - num_2) 

        return -heap[0] if len(heap) > 0 else 0
