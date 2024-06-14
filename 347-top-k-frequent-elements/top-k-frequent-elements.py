class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        res = []
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


        res = []
        count = Counter(nums)
        freq = [[] for _ in range(len(nums)+1)]
        for n, c in count.items():
            freq[c].append(n)
        
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
        
        min_heap = []
        look_up = Counter(nums)
        res = []

        for n, count in look_up.items():
            if len(min_heap) >= k:
                heapq.heappushpop(min_heap, (count, n))
            else:
                heapq.heappush(min_heap, (count, n))
        
        while k > 0:
            res.append(heapq.heappop(min_heap)[1])
            k -= 1
        return res

