class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        while len(stones) >= 2:
            stones.sort()
            stone_a = stones.pop()
            stone_b = stones.pop()
            new_stone = abs(stone_a - stone_b)
            stones.append(new_stone)
            
        
        return stones[0]
        
