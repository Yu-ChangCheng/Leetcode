class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

        """
        TTTT FFFF
           L R
        """
        n = len(position)
        position.sort()
        
        def count(d):
            ans, curr = 1, position[0]
            for i in range(1, n):
                if position[i] - curr >= d:
                    ans += 1
                    curr = position[i]
            return ans
        
        l, r = 0, position[-1] - position[0]
        while l < r:
            mid = r - (r - l) // 2
            if count(mid) >= m:
                l = mid
            else:
                r = mid - 1
        return l