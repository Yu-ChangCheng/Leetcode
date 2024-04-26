class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        min_heap = []
        look_up = Counter(nums)
        res = []

        for n, count in look_up.items():
            if len(min_heap) >= k:
                heapq.heappushpop(min_heap, (count, n))
            else:
                heapq.heappush(min_heap, (count, n))
        
        for i in range(k-1, -1, -1):
            res.append(min_heap[i][1])
        return res