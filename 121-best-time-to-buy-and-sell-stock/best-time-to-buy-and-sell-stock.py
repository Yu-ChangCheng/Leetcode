class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 1:
            return 0

        l = 0
        r = 1
        max_profit = 0

        while r <= len(prices) - 1 :
            if prices[l] < prices[r]:
                max_profit = max(max_profit, prices[r] - prices[l])
                r += 1     
            else:
                l = r
                r += 1
            
        return max_profit