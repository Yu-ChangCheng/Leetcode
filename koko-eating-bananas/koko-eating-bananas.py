class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = int(r)

        while l <= r:
            hours = 0
            m = (l + r) // 2
            for p in piles:
                hours += int(math.ceil(p/float(m)))

            if hours <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res
            