class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # prices = [7,1,5,3,6,4]
        maxProfit = 0
        l = 0
        r = 0
        while r < len(prices):
            if prices[l] <= prices[r]: # check if it is a valid window, keep moves the right pointer
                currProfit = prices[r] - prices[l]
                maxProfit = max(currProfit, maxProfit)
            else: # it is not a valid window move the left pointer
                l = r
            r += 1
        return maxProfit
        # TC: O(n) / SC: O(1)

            