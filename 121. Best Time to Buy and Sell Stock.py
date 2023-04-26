class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_Value = 10001
        profit = 0

        if len(prices) == 0:
            return 0

        for price in prices:
            if price < min_Value :
                min_Value = price
            elif price > min_Value:
                if price - min_Value > profit:
                    profit = price - min_Value
        return profit

##############################
#Failed
# Min = (0 , prices[0])
# Max = (0 , prices[0])
# profit = 0
# i = 1
# while i < len(prices):
#     if prices[i] < Min[1]:
#         Min = (i,prices[i])
#         print(Min)
#     if prices[i] > Max[1] & Max[0] >= Min[0]:
#         Max = (i, prices[i])
#
#         print(Max)
#     i += 1
# print ("ans: ", Max[1] - Min[1] ,"Max: ", Max,"Min: ", Min )

# #############################
# ans from leetcode
# prices = [9,8,7,6,5,4]
# if len(prices) == 0:
#     print (0)
#
# min_Value = 999999999 # represent minimum price so far
# # profit = 0
# for price in prices: # price = 9, 8
#     if price > min_Value: # 9 > 999999999 false, 8 > 9 false,
#         if price - min_Value > profit:
#             profit = price - min_Value
#     elif price < min_Value: # 9 < 999999999 true, 8 < 9 true
#         min_Value = price #min_Value = 9, min_Value = 8...
#
# print(profit) # profit = 0
# ############################
## ans from leetcode
# prices = [2,4,1]
# if len(prices) == 0:
#     print (0)
#
# min_Value = 999999999 # represent minimum price so far
# profit = 0
# for price in prices: # price = 2, 4, 1
#     if price > min_Value: # 2 > 999999999 false, 4 > 2 true, 1 > 2 false
#         if price - min_Value > profit: # 4 - 2 > 0 true
#             profit = price - min_Value # profit = 4-2 = 2
#     elif price < min_Value: # 2 < 999999999 true, 1 < 2 false
#         min_Value = price #min_Value = 2,
#
# print(profit) # profit = 0, 2
