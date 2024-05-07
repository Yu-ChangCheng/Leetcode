class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            first_stone = heapq.heappop(stones)
            second_stone = heapq.heappop(stones)
            diff = - abs(first_stone - second_stone)
            heapq.heappush(stones, diff)
        return -stones[0]
            
            