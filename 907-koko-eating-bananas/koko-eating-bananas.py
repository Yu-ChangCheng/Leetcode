class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l+r) // 2
            hours = 0
            for n in piles:
                hours += int(math.ceil(n/float(k)))
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res
                

            