class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            m = (l + r) // 2
            time = 0
            for n in piles:
                time += math.ceil(n / float(m))
            if time <= h:
                res = min(m, res)
                r = m - 1
            else:
                l = m + 1
        return res
            