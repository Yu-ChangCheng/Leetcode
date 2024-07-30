class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # [7,2,3,1,5,3,6,9]

        l = 0
        r = 0
        maxProfit = 0
        while r < len(prices):
            if prices[r] >= prices[l]: # if the right pointer is larger than the left, meaning valid window, move right pointer
                maxProfit = max(prices[r] - prices[l], maxProfit)
                r += 1 # 
            else: # else the window is not valid, move the left pointer
                l = r
                r = r + 1
        return maxProfit

        