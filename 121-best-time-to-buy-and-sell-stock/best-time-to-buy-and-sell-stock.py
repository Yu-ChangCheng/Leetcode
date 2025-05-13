class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        l = 0
        r = 0

        while r < len(prices):
            if prices[l] <= prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(currentProfit, maxProfit)
                r += 1
            else:
                l = r
                r += 1
        return maxProfit                
                
