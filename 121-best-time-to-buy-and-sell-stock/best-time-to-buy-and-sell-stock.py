class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        r = 0
        maxProfit = 0

        while r < len(prices) and l <= r:
            if prices[r] > prices[l]:
                maxProfit = max(prices[r] - prices[l], maxProfit)
                r += 1
            else:
                l = r
                r = l + 1

        return maxProfit
            